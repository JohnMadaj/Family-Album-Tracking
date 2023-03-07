import csv


class Tracker:
    def read(self, path):
        with open(path, 'r') as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter='\t')
            next(tsvreader)
            for line in tsvreader:
                if not len(line):
                    return
                Round_number = int(line[0])
                self.curr_Round = max(Round_number, self.curr_Round)
                self.scan_album(Round_number, self.dad_dict, line[1])
                self.scan_album(Round_number, self.mom_dict,line[2])
                self.scan_album(Round_number, self.jen_dict,line[3])
                self.scan_album(Round_number, self.justin_dict,line[4])
                self.scan_album(Round_number, self.patrick_dict,line[5])
                self.scan_album(Round_number, self.jack_dict,line[6])
                self.scan_album(Round_number, self.joey_dict,line[7])
                self.scan_album(Round_number, self.jakob_dict,line[8])
                # self.mom_dict[Round_number] = self.scan_album(line[2])
                # self.jen_dict[Round_number] = self.scan_album(line[3])
                # self.justin_dict[Round_number] = self.scan_album(line[4])
                # self.patrick_dict[Round_number] = self.scan_album(line[5])
                # self.jack_dict[Round_number] = self.scan_album(line[6])
                # self.joey_dict[Round_number] = self.scan_album(line[7])
                # self.jakob_dict[Round_number] = self.scan_album(line[8])

    def write_tsv_file(self, path=""):
        if not len(path):
            path=self.path
        with open(path, "w") as f:
            for line in self.__str__().split("\n"):
                f.write(line + "\n")

    def scan_album(self, round_num, fam, column):
        if column == "//":
            return
        column = column.split(" - ")
        artist = column[0]
        if len(column) == 2:
            album = column[1]
            fam[round_num] = [artist, album]
            return
        fam[round_num] = [artist]
        return

    def __init__(self, path):  # dict[Round num] = {artist:, album:, year:, genre:,}
        self.curr_Round = 0
        self.dad_dict = {"name":"Dad"}
        self.mom_dict = {"name":"Mom"}
        self.jen_dict = {"name":"Jen"}
        self.justin_dict = {"name":"Justin"}
        self.patrick_dict = {"name":"Patrick"}
        self.jack_dict = {"name":"Jack"}
        self.joey_dict = {"name":"Joey"}
        self.jakob_dict = {"name":"Jakob"}
        self.path = path
        self.family = {"Dad": self.dad_dict,
                       "Mom": self.mom_dict,
                       "Jen": self.jen_dict,
                       "Justin": self.justin_dict,
                       "Patrick": self.patrick_dict,
                       "Jack": self.jack_dict,
                       "Joey": self.joey_dict,
                       "Jakob": self.jakob_dict}
        self.read(self.path)

    def __str__(self):
        fam_string = "Round\t"
        for member in self.family.values():
            fam_string += "%s\t" % (member["name"])
        fam_string += "\n"
        for Round in range(1, self.curr_Round+1):
            fam_string += "%s\t" % (Round)
            for member in self.family.values():
                if Round in member:
                    sel = member[Round]
                    if len(sel) == 2:
                        selstr = sel[0] + " - " + sel[1]
                    else:
                        selstr = sel[0]
                    fam_string += str(selstr) + "\t"
                else:
                    fam_string += "//\t"
            fam_string += "\n"
        return fam_string

    # def get_selections(self, member):
    def add_selection(self, fam_name, artist, album="", track=""):
        try:
            fam = self.family[fam_name]
        except Exception as e:
            return "Not a family member"
        if self.curr_Round in fam: # fam member has a selection for this Round already
            # before moving to next Round, make sure everyone else has a selection for this Round
            for other_fam in self.family.values():
                # if someone doesnt, cancel the new selection, return a user instruction
                if self.curr_Round not in other_fam:
                    return "At least one family member doesnt have a selection for this Round yet, cant move to next " \
                           "Round"
            # now you can add a new Round
            self.curr_Round += 1
        fam[self.curr_Round] = [artist]
        if len(album):
            fam[self.curr_Round].append("A:"+album)
        elif len(track):
            fam[self.curr_Round].append("T:"+track)
        return


if __name__ == '__main__':
    t = Tracker("temp.tsv")
    while True:
        cmd = int(input("What to do?\n1 - Add Selection\n2 - Print Tracker\n3 - Write to File\n0 - Quit"))
        if not cmd:
            quit()
        elif cmd == 1:
            fam_member = input("Family member?")
            artist = input("Artist?")
            album = input("Album? (Enter if none)")
            track = input("Track? (Enter if none)")
            print(t.add_selection(fam_name=fam_member,
                                  artist=artist,
                                  album=album,
                                  track=track))
        elif cmd == 2:
            print(t)
        elif cmd == 3:
            t.write_tsv_file("tracker_output.tsv")
