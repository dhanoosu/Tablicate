import sys

class Column():

    justify_type = {
        ""      : '',
        "left" : '<',
        "right"  : '>',
        "center": '^'
    }

    def __init__(self, text, size, justify="", pad_text=False):
        self.text = text
        self.size = size

        if justify in self.justify_type:
            self.justify = justify
        else:
            print("[TABLICATE] ERROR: Invalid justify keyword: only {}".format(self.justify_type.key()))
            sys.exit(1)

        # Add 2 spaces paddings around the text
        if pad_text:
            self.text = "{1}{0}{1}".format(self.text, " "*2)

    def get_formatted_size(self, offset=0):

        return "{}{}".format(
            self.justify_type[self.justify],
            self.size + offset
        )

class Table():

    # if sys.version_info.major > 2:
    #     TOP_LEFT_CORNER     = '┏'
    #     TOP_RIGHT_CORNER    = '┓'
    #     BOTTOM_LEFT_CORNER  = '└'
    #     BOTTOM_RIGHT_CORNER = '┘'

    #     TOP_SEPARATOR       = '┳'
    #     LEFT_SEPARATOR      = '┡'
    #     RIGHT_SEPARATOR     = '┩'
    #     MIDDLE_SEPARATOR    = '╇'
    #     BOTTOM_SEPARATOR    = '┴'

    #     VERITCAL_LINE           = '│'
    #     HORIZONTAL_LINE         = '─'
    #     HORIZONTAL_BOLD_LINE    = '━'
    # else:
    TOP_LEFT_CORNER     = '+'
    TOP_RIGHT_CORNER    = '+'
    BOTTOM_LEFT_CORNER  = '+'
    BOTTOM_RIGHT_CORNER = '+'

    TOP_SEPARATOR       = '+'
    LEFT_SEPARATOR      = '+'
    RIGHT_SEPARATOR     = '+'
    MIDDLE_SEPARATOR    = '+'
    BOTTOM_SEPARATOR    = '+'

    VERITCAL_LINE           = '|'
    HORIZONTAL_LINE         = '-'
    HORIZONTAL_BOLD_LINE    = '-'



    def __init__(self, show_header=True, header_style=""):
        self.row_list = []
        self.header = []

        self.has_row = False

    def add_column(self, col, justify=""):

        self.header.append(
            Column(text=col, size=(4+len(str(col))), justify=justify, pad_text=True)
        )

    def add_row(self, row):

        self.has_row = True

        if len(row) != len(self.header):
            print("[TABLICATE] ERROR: no. row != no. header")
            sys.exit(1)
        else:
            new_row = []
            for r in row:
                new_row.append("{1}{0}{1}".format(r, " "*2))

            self.row_list.append(new_row)

    # def add_row_separator(self):

    def print_table(self, content=None):

        # Providing a content will overwrite the header and row information
        if content:

            # Clear header and row lists
            del self.header[:]
            del self.row_list[:]

            for (i, value_list) in enumerate(content):

                if i == 0:
                    for col in value_list:
                        self.add_column(col)
                else:
                    self.add_row(value_list)


        # Get max cell width
        for (i, col) in enumerate(zip(*self.row_list)):
            for c in col:
                if (len(c)) > self.header[i].size:
                     self.header[i].size = (len(c))

        h0_line = ""        # Line above heading
        h1_line = ""        # Line below heading
        middle_line = ""    # Lines between heading and bottom
        bottom_line = ""    # Bottom line

        for (i, h) in enumerate(self.header):

            if i == 0:
                h0_line     += "{}{}".format(self.TOP_LEFT_CORNER, self.HORIZONTAL_BOLD_LINE*(h.size))
                h1_line     += "{}{}".format(self.LEFT_SEPARATOR, self.HORIZONTAL_BOLD_LINE*(h.size))
                middle_line += "{}{}".format(self.LEFT_SEPARATOR, self.HORIZONTAL_LINE*(h.size))
                bottom_line += "{}{}".format(self.BOTTOM_LEFT_CORNER, self.HORIZONTAL_LINE*(h.size))
            elif i < (len(self.header)):
                h0_line     += "{}{}".format(self.TOP_SEPARATOR, self.HORIZONTAL_BOLD_LINE*(h.size))
                h1_line     += "{}{}".format(self.MIDDLE_SEPARATOR, self.HORIZONTAL_BOLD_LINE*(h.size))
                middle_line += "{}{}".format(self.MIDDLE_SEPARATOR, self.HORIZONTAL_LINE*(h.size))
                bottom_line += "{}{}".format(self.BOTTOM_SEPARATOR, self.HORIZONTAL_LINE*(h.size))


        h0_line += "{}".format(self.TOP_RIGHT_CORNER)
        h1_line += "{}".format(self.RIGHT_SEPARATOR)
        middle_line += "{}".format(self.RIGHT_SEPARATOR)
        bottom_line += "{}".format(self.BOTTOM_RIGHT_CORNER)

        # Prints first line no matter what
        print(h0_line)

        for h in self.header:

            # Justfication format -> |{:20} or |{:>20} or |{:^20}
            format_row = "{0}{{:{1}}}".format(self.VERITCAL_LINE, h.get_formatted_size(offset=0))
            print(format_row.format(h.text), end="")

        # Prints the last vertical line to finish header content
        print(self.VERITCAL_LINE)
        # Print a line below header
        print(h1_line)

        for t in self.row_list:
            for (i, r) in enumerate(t):
                h = self.header[i]

                format_row = "{0}{{:{1}}}".format(self.VERITCAL_LINE, h.get_formatted_size(offset=0))
                print(format_row.format(r), end="")

            print(self.VERITCAL_LINE)


        # Prints bottom line if there is any rows added
        if self.has_row:
            print(bottom_line)