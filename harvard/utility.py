from colorama import Fore, Back, Style

class Utility:
    
    @staticmethod
    def print_lines(lines: list):
        """
        Simple engine that prints formatted lines.
        
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
                elif line.startswith('@warning'):
                    line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                        color_fg = Fore.YELLOW, color_bg = Back.RED, reset_bg = Back.RESET, reset_fg = Fore.RESET)
                print(line)

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