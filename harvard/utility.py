from colorama import Fore, Back, Style
import re
import sys, inspect



class Utility:
    
    @staticmethod
    def interact(lines: list) -> str:
        """
        convenience method that calls automatically print_lines and prompt_user_for_input
        """
        options = Utility.print_lines(lines)
        return Utility.prompt_user_for_input(options = options if len(options)>0 else None)

    @staticmethod
    def print_lines(lines: list):
        """
        Simple engine that prints formatted lines.
        It returns all the [K]eys of the @option passed as argument
        
        Valid arguments are
        * a list of strings
        * a list of arrays of strings
        * a mix of the above

        Formatting options: prepend the line with a tag to format it automatically
        * @title: highlighted line
        * @subtitle: dimmed line
        * @option: intended dimmed line, part of a list
        * @warning: highlighted line with a red background
        """
        options = []
        for line in lines:
            if isinstance(line, list):
                Utility.print_lines(line)
            else:
                if line.startswith('@title'):
                    line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                        color_fg = Fore.BLACK, color_bg = Back.WHITE, reset_bg = Back.RESET, reset_fg = Fore.RESET)
                elif line.startswith('@subtitle'):
                    line = '{style}{line}{reset_st}'.format(line = line[len('@subtitle'):],style = Style.DIM, reset_st = Style.RESET_ALL)
                elif line.startswith('@option'):
                    line = '{style} - {line}{reset_st}'.format(line = line[len('@option'):],style = Style.DIM, reset_st = Style.RESET_ALL)
                    letter = Utility._extract_option_letter(line)
                    if letter is not None:
                        options.append(letter)
                elif line.startswith('@warning'):
                    line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                        color_fg = Fore.YELLOW, color_bg = Back.RED, reset_bg = Back.RESET, reset_fg = Fore.RESET)
                print(line)
        return options

    @staticmethod
    def _extract_option_letter(option: str) -> str:
        match = re.search(".*\[(\w)\].*", option)
        return match.group(1) if match is not None else None

    @staticmethod
    def prompt_user_for_input(text: str = None, options = None) -> str:
        """
        Utility method to get an option

        text: optional label. If absent options is printed instead
        options: array of accepted inputs. If specified, the user can only input one of the values
        """
        while True:
            user_input = input('{prompt} > '.format(prompt = text if text is not None else options if options is not None else ''))
            if options is None or user_input in options:
                return user_input if user_input != '' else None
            else:
                print('{color}Err. valid options are {options}{reset_fore}'.format(
                    color=Fore.RED, options = options, reset_fore = Fore.RESET))

    @staticmethod
    def find_classes(base_class: type):
        """
        use reflection to find all non-abstract classes extending clazz
        """
        lst = set()
        for _, module in inspect.getmembers(sys.modules['harvard']):
            if inspect.ismodule(module):
                for _, member in inspect.getmembers(module):
                    if inspect.isclass(member) and not inspect.isabstract(member) and issubclass(member, base_class):
                        lst.add(member)
        return list(lst)

        