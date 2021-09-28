from colorama import Fore, Back, Style
import re
import sys, inspect

class Utility:
    
    @staticmethod
    def interact(lines: list) -> str:
        """Convenience method that calls automatically print_lines and prompt_user_for_input

        Args:
            lines: each entry may be a str or a list. Lists are processed recursively
        returns:
            value inserted by the user or None
        """
        options = Utility.print_lines(lines)
        return Utility.prompt_user_for_input(options = options if len(options)>0 else None)

    @staticmethod
    def print_lines(lines: list):
        """Simple engine that prints formatted lines.
        
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

        Args:
            lines: each entry may be a str or a list. Lists are processed recursively
        Returns:
            list of valid Keys
        """
        options = []
        for line in lines:
            if isinstance(line, list):
                # it's a list: recursively process it
                Utility.print_lines(line)
            else:
                # print and extract keys
                opt = Utility.__print_formatted(line)
                if opt is not None:
                    options.append(opt)
        return options

    @staticmethod
    def __print_formatted(line):
        """Internal meathod to format lines according to a template
        
        see print_lines(...) for details
        
        Args:
            line: line to be formatted and printed
        Returns:
            key found in the option, or None
        """
        option = None
        if line.startswith('@title'):
            # format it with white background and black text
            line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                color_fg = Fore.BLACK, color_bg = Back.WHITE, reset_bg = Back.RESET, reset_fg = Fore.RESET)
        elif line.startswith('@subtitle'):
            # format it with a dimmed font
            line = '{style}{line}{reset_st}'.format(line = line[len('@subtitle'):],style = Style.DIM, reset_st = Style.RESET_ALL)
        elif line.startswith('@option'):
            # format it with a dimmed font and look for a key
            line = '{style} - {line}{reset_st}'.format(line = line[len('@option'):],style = Style.DIM, reset_st = Style.RESET_ALL)
            letter = Utility._extract_option_letter(line)
            if letter is not None:
                option = letter
        elif line.startswith('@warning'):
            # make it bright with red and yellow!
            line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@warning'):],
                color_fg = Fore.YELLOW, color_bg = Back.RED, reset_bg = Back.RESET, reset_fg = Fore.RESET)
        print(line)
        return option

    @staticmethod
    def _extract_option_letter(option: str) -> str:
        """Convenience method to estract the key from a string like '@option foo [B]ar'

        Args:
            option: option that may contain the key
        Returns:
            it returns the key in brakets or None
        """
        # match with a regex
        # format is "whatever[K]whatever"
        match = re.search(".*\[(\w)\].*", option)
        return match.group(1) if match is not None else None

    @staticmethod
    def prompt_user_for_input(text: str = None, options = None) -> str:
        """Utility method to get an option

        Args:
            text: optional label. If absent options is printed instead
            options: array of accepted inputs. If specified, the user can only input one of the values
        Returns:
            user input
        """
        while True:
            # infinite loop waiting for a valid input
            user_input = input('{prompt} > '.format(prompt = text if text is not None else options if options is not None else ''))
            if options is None or user_input in options:
                return user_input if user_input != '' else None
            else:
                # error, let the user know the valid options
                print('{color}Err. valid options are {options}{reset_fore}'.format(
                    color=Fore.RED, options = options, reset_fore = Fore.RESET))

    @staticmethod
    def find_classes(base_class: type):
        """Use reflection to find all non-abstract classes extending clazz

        Args:
            base_class: it will find non-abstract subclasses of this class
        Returns:
            list of classes
        """
        lst = set()
        # iterate over the content
        for _, module in inspect.getmembers(sys.modules['harvard']):
            if inspect.ismodule(module):
                # if it's a module, check the members
                for _, member in inspect.getmembers(module):
                    if inspect.isclass(member) and not inspect.isabstract(member) and issubclass(member, base_class):
                        # if it's a non-abstract subclass of base_class, add it to the list
                        lst.add(member)
        return list(lst)

        