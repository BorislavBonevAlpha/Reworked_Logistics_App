
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        print("\nHello and welcome to the logistics application. In here you can manage the functionality revolving around creating different routes with packages and customers. \n"
            "------------------------------------------------------------------------------------------------------------------------------------------------"
            "\nType your prefered command and after that put the correct parameters to it.\n"
            "------------------------------------------------------------------------------------------------------------------------------------------------"
            "\nCommand examples: createcustomer / createpackage / createroutes / searchroutes / viewpackage / viewroute / assingtruck / assingpackage \n"
            "------------------------------------------------------------------------------------------------------------------------------------------------")
        while True:
            
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line)
                output.append(command.execute())
            except ValueError as err:
                output.append(err.args[0])

        print('\n'.join(output))
