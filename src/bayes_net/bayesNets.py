import random

class BayesNets():
    """
    A class to represent a Bayes Network.

    ...

    Attributes
    ----------
    filepath : str
        The File Path in string from which the data have to be extracted.

    Methods
    -------
    extractRV(verbose = True) -> None:
        This Function is used to extract the total number of random variables 
        and also there character representation from the file.
        
    extractConditionalProbability(verbose = True) -> None:
        This Function is used to extract all the conditional probability 
        tables from the file and stores these information in the dictionary 
        and all the tables in a single dictionary.    
        
    extractQuery(verbose = True) -> None:
        This Function is used to extract the query which is to be calculated 
        from the file.
    
    queryInfo(verbose = True) -> None:
        This Function is used to further extract information from the 
        extracted query. It is used to extract the information about the 
        dependent and conditional random variables from the query.

    generateSample(verbose = False) -> dict:
        This Function is used to generate a single sample randomly but 
        probability of each random variable selection is uniform.
    
    generateWeightedSample(verbose = True) -> tuple:
        This Function is used to generate a single sample randomly, but the 
        evidence will be fixed and each time any evidence is seen then 
        update the weights.

    doPriorSampling(TOTAL_SAMPLE = 10000, verbose = True) -> None:
        This Function is used to calculate the answer using the Prior Sampling.
        This function will simulate the Prior Sampling to calculate the answer 
        of the query.
        
    doRejectionSampling(TOTAL_SAMPLE_REQUIRED = 10000, verbose = True) -> None:
        This Function is used to calculate the answer using the Rejection 
        Sampling. This function will simulate the Rejection Sampling to 
        calculate the answer of the query.    
        
    doLikelihoodWeighting(TOTAL_SAMPLE = 10000, verbose = True) -> None:
        This Function is used to calculate the answer using the Likelihood 
        Weighting Sampling Method. This function will simulate the Likelihood 
        Weighting Sampling Method to calculate the answer of the query.
    
    doGibbsSampling(verbose = True) -> None:
        This Function is used to calculate the answer using the Gibbs Sampling.
        This function will simulate the Gibbs Sampling to calculate the answer 
        of the query.   
        
    """

    def __init__(self, filepath):
        """
        Constructor Function which initialize all the required variables as well 
        as start extracting all the information from the file passed as an argument
        using appropriate functions.

        Args:
            filepath: string
                The File Path in string from which the data have to be extracted.

        Returns:
            None

        Raises:
            FileNotFoundError: Raises an exception.
                File Does Not Exists or The Path is Wrong.
        """
        # Try Block to open the file.
        try:
            self.File = open(filepath, "r")
        except:
            # Raise the Error
            raise FileNotFoundError(
                "File Does Not Exists or The Path is Wrong.")
        else:
            # The Number of Random Variables.
            self.TotalRandomVariable = 0
            
            # The Information about the Random Variables
            self.RandomVariables = dict()
            
            # Extract the Information related to the Random Variables.
            self.extractRV()
            
            # Store the Conditional Probability in a Dictionary.
            self.ConditionalProbabilityTables = dict()
            
            # Store the Header Information in a Dictionary.
            self.ConditionalProbabilityHeader = dict()
            
            # Extract the Conditional Probability Tables from the file.
            self.extractConditionalProbability()
            
            # Store the Query.
            self.Query = ""
            self.ActualQuery = ""
            
            # Extract the Query from the file.
            self.extractQuery()
            
            # Since we had extracted all the information from the file, let's
            # close the file.
            self.File.close()
            
            # Store the Conditional Variables and the Dependent Variables.
            self.ConditionalVariables = dict()
            self.DependentVariables = dict()
            
            # Extract the Conditional Variables and the Dependent Variables.
            self.queryInfo()

    def __str__(self):
        """
        This method returns the string representation of the object. This method 
        is called when print() or str() function is invoked on an object. This 
        method must return the String object.
        """
        return (
            "-" * 60 + "\n" +
            f"Total Number of Random Variable: {self.TotalRandomVariable}\n" +
            "-" * 60 + "\n" +
            f"All Possible Random Variable Values: {self.RandomVariables}\n" +
            "-" * 60 + "\n" +
            f"Extracted Conditional Probability Header:\n{self.ConditionalProbabilityHeader}\n"
            + "-" * 60 + "\n" +
            f"Extracted Conditional Probability Tables:\n{self.ConditionalProbabilityTables}\n"
            + "-" * 60 + "\n" + f"Extracted Query: {self.Query}\n" + "-" * 60 +
            "\n" +
            f"Extracted Condition form the Query: {self.ActualQuery}\n" +
            "-" * 60 + "\n" +
            f"Final Extracted Conditional Values from the Query:\n {self.ConditionalVariables}\n"
            + "-" * 60 + "\n" +
            f"Final Extracted Depended Values from the Query:\n {self.DependentVariables}\n"
            + "-" * 60 + "\n")

    def extractRV(self, verbose=True) -> None:
        """
        This Function is used to extract the total number of random variables and also 
        there character representation from the file.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns:
            None

        Raises:
            ---
        """
        if verbose:
            print("Extracting The Random Variable Info...")
            
            # Read the line from the file.
            rv = self.File.readline().strip().split(',')
            print("Extracted The Random Variable Info from The File.")
            print(f"Info Extracted: {rv}")
            
            # convert it into a int.
            self.TotalRandomVariable = int(rv[0])
            print(
                f"Total Number of Random Variable: {self.TotalRandomVariable}")
            print("Start Extracting Random variables Possible Values...")
            
            # Extract all the possible option for the random variable.
            for i in range(self.TotalRandomVariable):
                self.RandomVariables[rv[i + 1].replace(" ", "")] = list()
            for j in range(self.TotalRandomVariable):
                extract = self.File.readline().strip().split(',')
                print(extract)
                for k in range(1, len(extract)):
                    self.RandomVariables[extract[0]].append(extract[k].replace(
                        " ", ""))
            print("Done Extracting Random variables Possible Values.")
            print(f"Possible Random Variable Values: {self.RandomVariables}\n")
        else:
            # Read the line from the file.
            rv = self.File.readline().strip().split(',')
            
            # convert it into a int.
            self.TotalRandomVariable = int(rv[0])
            
            # Extract all the possible option for the random variable.
            for i in range(self.TotalRandomVariable):
                self.RandomVariables[rv[i + 1].replace(" ", "")] = list()
            for j in range(self.TotalRandomVariable):
                extract = self.File.readline().strip().split(',')
                print(extract)
                for k in range(1, len(extract)):
                    self.RandomVariables[extract[0]].append(extract[k].replace(
                        " ", ""))

    def extractConditionalProbability(self, verbose=True) -> None:
        """
        This Function is used to extract all the conditional probability tables 
        from the file and stores these information in the dictionary and all the
        tables in a single dictionary.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns:
            None

        Raises:
            ---
        """
        if verbose:
            # get the Conditional Probability table.
            print("Start Extracting the Conditional Probability Table...")
            for i in range(self.TotalRandomVariable):
                about = self.File.readline().strip().split('|')
                print("-----------------------------")
                print(about)
                case = about[0].replace(' ', '')
                # variable = list()
                variable = about[-1].split(',')
                try:
                    variable = variable.remove('')
                    if variable == None:
                        variable = []
                except:
                    pass
                # Store the Conditional Probability in a Dictionary.
                self.ConditionalProbabilityTables[case] = dict()
                
                # Store the Header Information in a Dictionary.
                self.ConditionalProbabilityHeader[case] = list()
                print(variable)
                
                # store the header
                for head in variable:
                    self.ConditionalProbabilityHeader[case].append(
                        head.replace(' ', ''))
                
                # Iterate over the tables.
                for j in range(2**(len(variable) + 1)):
                    row = self.File.readline().strip().split(',')
                    print(row)
                    key = ""
                    for k in range(len(variable) + 1):
                        key += row[k].replace(' ', '')
                        key += " "
                    key = key[:-1]
                    probability = float(row[-1].replace(' ', ''))
                    # HashValueOfKey = hash(key)
                    self.ConditionalProbabilityTables[case][key] = probability
                print("-----------------------------")

            print(
                "Done Extracting the Conditional Probability Table from The File..."
            )
            print("***************************************")
            print(
                f"Extracted Conditional Probability Header: {self.ConditionalProbabilityHeader}"
            )
            print("***************************************")
            print(
                f"Extracted Conditional Probability Tables: {self.ConditionalProbabilityTables}"
            )
            print("***************************************\n")
        else:
            # get the Conditional Probability table.
            for i in range(self.TotalRandomVariable):
                about = self.File.readline().strip().split('|')
                case = about[0].replace(' ', '')
                # variable = list()
                variable = about[-1].split(',')
                try:
                    variable = variable.remove('')
                    if variable == None:
                        variable = []
                except:
                    pass
                # Store the Conditional Probability in a Dictionary.
                self.ConditionalProbabilityTables[case] = dict()
                
                # Store the Header Information in a Dictionary.
                self.ConditionalProbabilityHeader[case] = list()
                
                # store the header
                for head in variable:
                    self.ConditionalProbabilityHeader[case].append(
                        head.replace(' ', ''))

                # Iterate over the tables.
                for j in range(2**(len(variable) + 1)):
                    row = self.File.readline().strip().split(',')
                    key = ""
                    for k in range(len(variable) + 1):
                        key += row[k].replace(' ', '')
                        key += " "
                    key = key[:-1]
                    probability = float(row[-1].replace(' ', ''))
                    # HashValueOfKey = hash(key)
                    self.ConditionalProbabilityTables[case][key] = probability

    def extractQuery(self, verbose=True) -> None:
        """
        This Function is used to extract the query which is to be calculated from 
        the file.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns:
            None

        Raises:
            ---
        """
        if verbose:
            # Get the query from the file
            print("Start Extracting the Query from The File...")
            self.Query = self.File.readline().strip().split(": ")[-1]
            
            # print(type(Query))
            print("Done Extracting the Query from the File.")
            print(f"Extracted Query: {self.Query}")
            self.ActualQuery = self.Query[2:-1].replace(' ', '')
            print(f"Extracted Condition form the Query: {self.ActualQuery}\n")
        else:
            # Get the query from the file
            self.Query = self.File.readline().strip().split(": ")[-1]
            
            # print(type(Query))
            self.ActualQuery = self.Query[2:-1].replace(' ', '')

    def queryInfo(self, verbose=True) -> None:
        """
        This Function is used to further extract information from the extracted 
        query. It is used to extract the information about the dependent and 
        conditional random variables from the query.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns:
            None

        Raises:
            ---
        """
        if verbose:
            print("Start Extracting More Information From the Query...")
            
            # split the data into Conditional and Dependent Variables.
            variables = self.ActualQuery.split('|')
            if len(variables) == 2:
                conditionalVariables = variables[0]
                print(
                    "-------------------------------------------------------------------"
                )
                print(f"The Conditional Variables: {conditionalVariables}")
                dependentVariables = variables[1]
                print(f"The Dependent Variables: {dependentVariables}")
                print(
                    "-------------------------------------------------------------------"
                )
                
                # Now, extract them further.
                conditionalVariables = conditionalVariables.split(',')
                dependentVariables = dependentVariables.split(',')
                print(
                    "Extraction information for Conditional Variables From the Query..."
                )
                for i in conditionalVariables:
                    var, val = tuple(i.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.ConditionalVariables[var] = val
                print(
                    f"Final Extracted Conditional Values from the Query:\n {self.ConditionalVariables}"
                )
                print(
                    "-------------------------------------------------------------------"
                )
                print(
                    f"Extraction information for Depended Variables From the Query..."
                )
                for j in dependentVariables:
                    var, val = tuple(j.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.DependentVariables[var] = val
                print(
                    f"Final Extracted Depended Values from the Query:\n {self.DependentVariables}"
                )
                print(
                    "-------------------------------------------------------------------\n"
                )

            else:
                conditionalVariables = variables[0]
                print(f"The Conditional Variables: {conditionalVariables}")
                dependentVariables = None
                print(f"The Dependent Variables: {dependentVariables}")
                conditionalVariables = conditionalVariables.split(',')
                dependentVariables = dependentVariables.split(',')
                print(
                    "Extraction information for Conditional Variables From the Query..."
                )
                for i in conditionalVariables:
                    var, val = tuple(i.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.ConditionalVariables[var] = val
                print(
                    f"Final Extracted Conditional Values from the Query:\n {self.ConditionalVariables}"
                )
                print(
                    "-------------------------------------------------------------------"
                )
                print(
                    f"Extraction information for Depended Variables From the Query..."
                )
                print(
                    f"Final Extracted Depended Values from the Query:\n {self.DependentVariables}"
                )
                print(
                    "-------------------------------------------------------------------\n"
                )

        else:
            # split the data into Conditional and Dependent Variables.
            variables = self.ActualQuery.split('|')
            if len(variables) == 2:
                conditionalVariables = variables[0]
                dependentVariables = variables[1]
                
                # Now, extract them further.
                conditionalVariables = conditionalVariables.split(',')
                dependentVariables = dependentVariables.split(',')
                for i in conditionalVariables:
                    var, val = tuple(i.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.ConditionalVariables[var] = val
                for j in dependentVariables:
                    var, val = tuple(j.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.DependentVariables[var] = val
            else:
                conditionalVariables = variables[0]
                dependentVariables = None
                conditionalVariables = conditionalVariables.split(',')
                dependentVariables = dependentVariables.split(',')
                for i in conditionalVariables:
                    var, val = tuple(i.split('='))
                    var.replace(' ', '')
                    val.replace(' ', '')
                    self.ConditionalVariables[var] = val

    def generateSample(self, verbose=False) -> dict:
        """
        This Function is used to generate a single sample randomly but probability 
        of each random variable selection is uniform.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns: dictionary
            The dictionary contain the random variables as key and the value as 
            the selected option of the random variable.
            example: {'B': '-b', 'E': '-e', 'A': '-a', 'J': '-j', 'M': '-m'}

        Raises:
            ---
        """
        # Store the sample in the dictionary.
        sample_visited = dict()
        if (not verbose):
            # iterate over all the random variables.
            for i in self.ConditionalProbabilityHeader:
                #     print(i)
                # Uniform Probability.
                probability = random.uniform(0, 1)
                #     print(probability)
                if len(self.ConditionalProbabilityHeader[i]) == 0:
                    # Choose the variable for a particular random variable using
                    # the uniform probability.
                    if self.ConditionalProbabilityTables[i][
                            self.RandomVariables[i][0]] > probability:
                        sample_visited[i] = self.RandomVariables[i][0]
                    else:
                        sample_visited[i] = self.RandomVariables[i][1]
                else:
                    # if the table is a conditional probability table, join the
                    # required sample calculated/chosen till now to select from
                    # the giver uniform probability.
                    sample = ""
                    for j in self.ConditionalProbabilityHeader[i]:
                        sample += sample_visited[j] + " "
                    possibility = []
                    for k in self.RandomVariables[i]:
                        possibility.append(sample + k)
                    if self.ConditionalProbabilityTables[i][
                            possibility[0]] > probability:
                        sample_visited[i] = self.RandomVariables[i][0]
                    else:
                        sample_visited[i] = self.RandomVariables[i][1]
        else:
            print("\nStarted Generating a Single Sample...")
            # iterate over all the random variables.
            for i in self.ConditionalProbabilityHeader:
                #     print(i)
                # Uniform Probability.
                probability = random.uniform(0, 1)
                #     print(probability)
                if len(self.ConditionalProbabilityHeader[i]) == 0:
                    # Choose the variable for a particular random variable using
                    # the uniform probability.
                    if self.ConditionalProbabilityTables[i][
                            self.RandomVariables[i][0]] > probability:
                        sample_visited[i] = self.RandomVariables[i][0]
                    else:
                        sample_visited[i] = self.RandomVariables[i][1]
                else:
                    # if the table is a conditional probability table, join the
                    # required sample calculated/chosen till now to select from
                    # the giver uniform probability.
                    sample = ""
                    for j in self.ConditionalProbabilityHeader[i]:
                        sample += sample_visited[j] + " "
                    possibility = []
                    for k in self.RandomVariables[i]:
                        possibility.append(sample + k)
                    if self.ConditionalProbabilityTables[i][
                            possibility[0]] > probability:
                        sample_visited[i] = self.RandomVariables[i][0]
                    else:
                        sample_visited[i] = self.RandomVariables[i][1]
            
                # Print the sample constructed till now.
                print(
                    "---------------------------------------------------------------------------------"
                )
                print(
                    f"With Probability {probability}: {sample_visited} is chosen till now..."
                )
            
            # print the final sample generated.
            print(
                "*********************************************************************************"
            )
            print(f"Final Sample Generated: {sample_visited}")
            print(
                "*********************************************************************************\n"
            )
        
        # return the sample.
        return sample_visited

    def doPriorSampling(self, TOTAL_SAMPLE=10000, verbose=True) -> None:
        """
        This Function is used to calculate the answer using the Prior Sampling.
        This function will simulate the Prior Sampling to calculate the answer 
        of the query.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.
            
            TOTAL_SAMPLE: Int
                Default: 10000
                Run the simulation for total TOTAL_SAMPLE iterations, and generate 
                a total of TOTAL_SAMPLE samples.

        Returns:
            None
                
        Raises:
            ---
        """
        # total number of sample with all the requirement fulfilled.
        requiredSample = 0
        
        # total number of sample where the evidence is seen.
        evidence = 0
        if (verbose):
            print(
                "------------ CALCULATE THE QUERY USING PRIOR SAMPLING ------------"
            )
            print("Started Generating The Sample...")
            
            # Iterate for TOTAL_SAMPLE of times.
            for iteration in range(1, TOTAL_SAMPLE + 1):
                # generate a single sample.
                sample = self.generateSample()
                if len(self.DependentVariables) > 0:
                    flag = True
                    
                    # check for the evidence.
                    for key, value in self.DependentVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        evidence += 1
                        flag = True
                        
                        # check for the required sample.
                        for key, value in self.ConditionalVariables.items():
                            if value != sample[key]:
                                flag = False
                                break
                        if flag:
                            requiredSample += 1

                    # After every 100 iteration print the current status.
                    if iteration % 100 == 0:
                        print("************************************")
                        print(f"STATUS: Iteration Number -->{iteration}<--")
                        print(f"Evidence Seen: {evidence}")
                        print(f"Required Sample Seen: {requiredSample}")
                        print("************************************")

                else:
                    flag = True
                    
                    # check for the required sample.
                    for key, value in self.ConditionalVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        requiredSample += 1

                    # After every 100 iteration print the current status.
                    if iteration % 100 == 0:
                        print("************************************")
                        print(f"STATUS: Iteration Number -->{iteration}<--")
                        print(f"Required Sample Seen: {requiredSample}")
                        print("************************************")

        else:
            print(
                "------------ CALCULATE THE QUERY USING PRIOR SAMPLING ------------"
            )
            
            # Iterate for TOTAL_SAMPLE of times.
            for iteration in range(1, TOTAL_SAMPLE + 1):
                # generate a single sample.
                sample = self.generateSample()
                if len(self.DependentVariables) > 0:
                    flag = True
                    
                    # check for the evidence.
                    for key, value in self.DependentVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        evidence += 1
                        flag = True
                       
                        # check for the required sample.
                        for key, value in self.ConditionalVariables.items():
                            if value != sample[key]:
                                flag = False
                                break
                        if flag:
                            requiredSample += 1

                else:
                    flag = True
                    
                    # check for the required sample.
                    for key, value in self.ConditionalVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        requiredSample += 1

        # Print the final Result.
        print(
            "------------------------------------------------------------------"
        )
        print(f"Completed {TOTAL_SAMPLE} Iterators of Sampling.")
        print("Final Result:")
        print(f"Total Sample Generated = {TOTAL_SAMPLE}")
        print(
            f"Total Required Sample Seen: {self.ConditionalVariables} | {self.DependentVariables} = {requiredSample}"
        )
        if len(self.DependentVariables) > 0:
            print(
                f"Total Evidence Seen: {self.DependentVariables} = {evidence}")
            print(f"Probability = {requiredSample/evidence}")
        else:
            print(f"Probability = {requiredSample/TOTAL_SAMPLE}")
        print(
            "------------------------------------------------------------------\n"
        )

    def doRejectionSampling(self,
                            TOTAL_SAMPLE_REQUIRED=10000,
                            verbose=True) -> None:
        """
        This Function is used to calculate the answer using the Rejection Sampling.
        This function will simulate the Rejection Sampling to calculate the answer 
        of the query.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.
            
            TOTAL_SAMPLE_REQUIRED: Int
                Default: 10000
                Run the simulation till the program had seen a total of 
                TOTAL_SAMPLE_REQUIRED evidences, and the function will keep on
                generation samples until the total number of evidence are seen.

        Returns:
            None
                
        Raises:
            ---
        """
        # number of total sample generated.
        total_sample_generated = 0
        
        # number of total required sample seen.
        total_seen_sample = 0
        
        # number of times evidence is seen.
        evidence = 0
        if (verbose):
            print(
                "------------ CALCULATE THE QUERY USING REJECTION SAMPLING ------------"
            )
            print("Started Generating The Sample...")
            
            # keep on generating sample until meet a particulate condition.
            while (True):
                # Count the total number of sample generated.
                total_sample_generated += 1
                
                # generate a single sample.
                sample = self.generateSample()
                if len(self.DependentVariables) > 0:
                    flag = True
                    
                    # check for the evidence.
                    for key, value in self.DependentVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        evidence += 1
                        flag = True
                        
                        # check for the required sample.
                        for key, value in self.ConditionalVariables.items():
                            if value != sample[key]:
                                flag = False
                                break
                        
                        # increase the count of total_seen_sample by 1.
                        if flag:
                            total_seen_sample += 1

                    # After every 1000 iteration print the current status.
                    if total_sample_generated % 1000 == 0:
                        print("************************************")
                        print(
                            f"STATUS: Iteration Number -->{total_sample_generated}<--"
                        )
                        print(
                            f"Total Sample Generated: {total_sample_generated}"
                        )
                        print(
                            f"Total Sample Rejected: {total_sample_generated - evidence}"
                        )
                        print(f"Total Sample Accepted: {evidence}")
                        print(f"Evidence Seen: {evidence}")
                        print(f"Required Sample Seen: {total_seen_sample}")
                        print("************************************")

                else:
                    flag = True
                    
                    # check for the required sample.
                    for key, value in self.ConditionalVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    
                    # increase the count of total_seen_sample and evidence by 1.
                    if flag:
                        total_seen_sample += 1
                        evidence += 1

                    # After every 1000 iteration print the current status.
                    if total_sample_generated % 1000 == 0:
                        print("************************************")
                        print(
                            f"STATUS: Iteration Number -->{total_sample_generated}<--"
                        )
                        print(
                            f"Total Sample Generated: {total_sample_generated}"
                        )
                        print(
                            f"Total Sample Rejected: {total_sample_generated - total_seen_sample}"
                        )
                        print(f"Total Sample Accepted: {evidence}")
                        print(f"Required Sample Seen: {total_seen_sample}")
                        print("************************************")

                # if we have seen the required amount of evidence, then break.
                if evidence == TOTAL_SAMPLE_REQUIRED:
                    break

        else:
            print(
                "------------ CALCULATE THE QUERY USING REJECTION SAMPLING ------------"
            )
            while (True):
                # Count the total number of sample generated.
                total_sample_generated += 1
                
                # generate a single sample.
                sample = self.generateSample()
                if len(self.DependentVariables) > 0:
                    flag = True
                    
                    # check for the evidence.
                    for key, value in self.DependentVariables.items():
                        if value != sample[key]:
                            flag = False
                            break
                    if flag:
                        evidence += 1
                        flag = True
                        
                        # check for the required sample.
                        for key, value in self.ConditionalVariables.items():
                            if value != sample[key]:
                                flag = False
                                break
                        if flag:
                            total_seen_sample += 1

                else:
                    flag = True
                    
                    # check for the required sample.
                    for key, value in self.ConditionalVariables.items():
                        if value != sample[key]:
                            flag = False
                            break

                    # increase the count of total_seen_sample and evidence by 1.
                    if flag:
                        total_seen_sample += 1
                        evidence += 1

                # if we have seen the required amount of evidence, then break.
                if evidence == TOTAL_SAMPLE_REQUIRED:
                    break

        # Print the final result.
        print("-----------------------------------------------------------")
        print(f"Completed {total_sample_generated} Iterators of Sampling.")
        print("Final Result:")
        print(f"Total Sample Generated = {total_sample_generated}")
        print(
            f"Total Sample Rejected = {total_sample_generated - total_seen_sample}"
        )
        print(f"Total Sample Accepted = {evidence}")
        # print(f"Total Evidence Seen = {evidence}")
        print(
            f"Total Required Sample Seen: {self.ConditionalVariables} | {self.DependentVariables} = {total_seen_sample}"
        )
        if len(self.DependentVariables) > 0:
            print(
                f"Total Evidence Seen: {self.DependentVariables} = {evidence}")
            print(f"Probability = {total_seen_sample/TOTAL_SAMPLE_REQUIRED}")
        else:
            print(f"Probability = {total_seen_sample/total_sample_generated}")
        print("-----------------------------------------------------------\n")

    def generateWeightedSample(self, verbose=True) -> tuple:
        """
        This Function is used to generate a single sample randomly, but the evidence
        will be fixed and each time any evidence is seen then update the weights.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.

        Returns: tuple
            The tuple contain a dictionary which contains the random variables as 
            key and the value as the selected option of the random variable, as 
            well the final weight. 
            example: ({'B': '-b', 'E': '-e', 'A': '-a', 'J': '+j', 'M': '-m'}, 0.05)

        Raises:
            ---
        """
        # Store the sample in the dictionary.
        sample_visited = dict()
        
        # Store the weights.
        sample_weight = 1
        if (not verbose):
            for i in self.ConditionalProbabilityHeader:
                #     print(i)
                if i not in self.DependentVariables:
                    probability = random.uniform(0, 1)
                    #     print(probability)
                    if len(self.ConditionalProbabilityHeader[i]) == 0:
                        if self.ConditionalProbabilityTables[i][
                                self.RandomVariables[i][0]] > probability:
                            sample_visited[i] = self.RandomVariables[i][0]
                        else:
                            sample_visited[i] = self.RandomVariables[i][1]
                    else:
                        sample = ""
                        for j in self.ConditionalProbabilityHeader[i]:
                            sample += sample_visited[j] + " "
                        possibility = []
                        for k in self.RandomVariables[i]:
                            possibility.append(sample + k)
                        if self.ConditionalProbabilityTables[i][
                                possibility[0]] > probability:
                            sample_visited[i] = self.RandomVariables[i][0]
                        else:
                            sample_visited[i] = self.RandomVariables[i][1]
                else:
                    # Fix the Evidence.
                    if len(self.ConditionalProbabilityHeader[i]) >= 0:
                        sample_visited[i] = self.DependentVariables[i]
                        sample = ""
                        for j in self.ConditionalProbabilityHeader[i]:
                            sample += sample_visited[j] + " "
                        sample += self.DependentVariables[i]
                        sample_weight *= self.ConditionalProbabilityTables[i][
                            sample]
                    sample_visited[i] = self.DependentVariables[i]

        else:
            print("\nStarted Generating a Single Sample...")
            for i in self.ConditionalProbabilityHeader:
                #     print(i)
                if i not in self.DependentVariables:
                    probability = random.uniform(0, 1)
                    #     print(probability)
                    if len(self.ConditionalProbabilityHeader[i]) == 0:
                        if self.ConditionalProbabilityTables[i][
                                self.RandomVariables[i][0]] > probability:
                            sample_visited[i] = self.RandomVariables[i][0]
                        else:
                            sample_visited[i] = self.RandomVariables[i][1]
                    else:
                        sample = ""
                        for j in self.ConditionalProbabilityHeader[i]:
                            sample += sample_visited[j] + " "
                        possibility = []
                        for k in self.RandomVariables[i]:
                            possibility.append(sample + k)
                        if self.ConditionalProbabilityTables[i][
                                possibility[0]] > probability:
                            sample_visited[i] = self.RandomVariables[i][0]
                        else:
                            sample_visited[i] = self.RandomVariables[i][1]
                    print(
                        "---------------------------------------------------------------------------------"
                    )
                    print(
                        f"With Probability {probability}: {sample_visited} is chosen till now..."
                    )
                else:
                    # Fix the Evidence.
                    print(
                        "---------------------------------------------------------------------------------"
                    )
                    print(
                        f"Fixing The Sample: {i} = {self.DependentVariables[i]}"
                    )
                    if len(self.ConditionalProbabilityHeader[i]) >= 0:
                        sample = ""
                        for j in self.ConditionalProbabilityHeader[i]:
                            sample += sample_visited[j] + " "
                        sample += self.DependentVariables[i]
                        sample_weight *= self.ConditionalProbabilityTables[i][
                            sample]
                    sample_visited[i] = self.DependentVariables[i]
                    print(f"Sample Chosen Till Now: {sample_visited}")
                    print(f"Updated Sample Weights are: {sample_weight}")
            print(
                "*********************************************************************************"
            )
            print(f"Final Sample Generated: {sample_visited}")
            print(f"Final Weight: {sample_weight}")
            print(
                "*********************************************************************************\n"
            )
        
        # return the sample generated and the final weight.
        return (sample_visited, sample_weight)

    def doLikelihoodWeighting(self, TOTAL_SAMPLE=10000, verbose=True) -> None:
        """
        This Function is used to calculate the answer using the Likelihood Weighting
        Sampling Method. This function will simulate the Likelihood Weighting
        Sampling Method to calculate the answer of the query.

        Args:
            verbose: bool
                Print the log details to understand what exactly the function is
                doing as well as to understand the flow of the program.
            
            TOTAL_SAMPLE: Int
                Default: 10000
                Run the simulation for total TOTAL_SAMPLE iterations, and generate 
                a total of TOTAL_SAMPLE weighted samples.

        Returns:
            None
                
        Raises:
            ---
        """
        # total required sample weight.
        requiredSampleWeight = 0.0
        
        # total evidence weight.
        evidenceWeight = 0.0
        if (verbose):
            print(
                "------------ CALCULATE THE QUERY USING LIKELIHOOD WEIGHTING ------------"
            )
            print("Started Generating The Sample...")
            
            # iterate for exact TOTAL_SAMPLE number of times.
            for iteration in range(1, TOTAL_SAMPLE + 1):
                # generate a single weighted sample.
                sample, weight = self.generateWeightedSample(verbose=False)
                evidenceWeight += weight
                flag = True
                
                # check for the required sample.
                for key, value in self.ConditionalVariables.items():
                    if value != sample[key]:
                        flag = False
                        break
                if flag:
                    # increment the requiredSampleWeight by the weight.
                    requiredSampleWeight += weight

                # After every 100 iteration print the current status.
                if iteration % 100 == 0:
                    print("************************************")
                    print(f"STATUS: Iteration Number -->{iteration}<--")
                    print(f"Total Evidence Weight: {evidenceWeight}")
                    print(
                        f"Total Required Sample Weight: {requiredSampleWeight}"
                    )
                    print("************************************")

        else:
            print(
                "------------ CALCULATE THE QUERY USING LIKELIHOOD WEIGHTING ------------"
            )
            # iterate for exact TOTAL_SAMPLE number of times.
            for iteration in range(1, TOTAL_SAMPLE + 1):
                # generate a single weighted sample.
                sample, weight = self.generateWeightedSample(verbose=False)
                evidenceWeight += weight
                flag = True
                
                # check for the required sample.
                for key, value in self.ConditionalVariables.items():
                    if value != sample[key]:
                        flag = False
                        break
                if flag:
                    # increment the requiredSampleWeight by the weight.
                    requiredSampleWeight += weight

        # Print the final OUTPUT.
        print(
            "------------------------------------------------------------------"
        )
        print(f"Completed {TOTAL_SAMPLE} Iterators of Sampling.")
        print("Final Result:")
        print(f"Total Sample Generated = {TOTAL_SAMPLE}")
        print(
            f"Total Required Sample Weight Seen: {self.ConditionalVariables} | {self.DependentVariables} = {requiredSampleWeight}"
        )
        print(
            f"Total Evidence Weight Seen: {self.DependentVariables} = {evidenceWeight}"
        )
        print(f"Probability = {requiredSampleWeight/evidenceWeight}")
        print(
            "------------------------------------------------------------------\n"
        )

    def doGibbsSampling(self, verbose=True):
        """
        This Function is used to calculate the answer using the Gibbs Sampling.
        This function will simulate the Gibbs Sampling to calculate the answer 
        of the query.
        """
        print("Not Yet Implemented!")
        pass