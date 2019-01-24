from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Block import Block


queues = {"0": "Custom", "1": "Normal (Blind Pick)", "2": "Normal 5v5 Blind Pick", "4": "Classic 5v5 Ranked Solo", "982": "Star Guardian Invasion: Normal", "6": "Ranked Premade 5v5", "7": "Co-op vs AI 5v5", "8": "Normal 3v3 Blind Pick", "9": "3v3 Ranked Flex", "14": "Normal 5v5 Draft Pick", "16": "Dominion Blind Pick 5v5", "17": "Dominion Draft Pick 5v5", "25": "Dominion Co-op vs AI", "31": "Co-op vs AI Intro Bot", "800": "Co-op vs. AI Intermediate Bot", "33": "Co-op vs AI Intermediate Bot", "34": "Intro", "35": "Beginner", "36": "Intermediate", "41": "3v3 Ranked Team", "42": "5v5 Ranked Team", "300": "Legend of the Poro King", "301": "Legend of the Poro King", "52": "Beginner Co-op vs AI", "310": "Nemesis", "820": "Co-op vs. AI Beginner Bot", "313": "Black Market Brawlers", "314": "Nexus Siege", "315": "Nexus Siege", "316": "Definitely Not Dominion", "61": "Team Builder 5v5", "62": "ARAM", "63": "ARAM", "64": "ARAM", "321": "Blood Hunt Assassin", "324": "ARSR", "325": "ARSR", "70": "One for All", "72": "Snowdown Showdown 1v1", "73": "Snowdown Showdown 2v2", "75": "Hexakill 6v6", "76": "Ultra Rapid Fire", "98": "Hexakill 6v6", "78": "Mirrored One for All", "850": "Co-op vs. AI Intermediate Bot", "83": "Co-op vs AI Ultra Rapid Fire", "600": "Blood Hunt Assassin", "601": "Blood Hunt Assassin", "90": "The Teemoing", "91": "Doom Bots Rank 1", "92": "Doom Bots Rank 2", "93": "Doom Bots Rank 5", "96": "Ascension", "97": "Ascension", "610": "Dark Star: Singularity", "611": "Dark Star: Singularity", "100": "5v5 ARAM Butcher's Bridge", "317": "Definitely Not Dominion", "318": "AR Ultra Rapid Fire", "319": "AR Ultra Rapid Fire", "320": "Blood Hunt Assassin", "900": "AR Ultra Rapid Fire", "901": "AR Ultra Rapid Fire", "65": "ARAM", "910": "Ascension", "911": "Ascension", "400": "Normal 5v5 Draft Pick", "401": "Normal (Draft Pick)", "402": "Normal (Draft Pick)", "403": "Normal (Draft Pick)", "920": "Legend of the Poro King", "921": "Legend of the Poro King", "410": "5v5 Ranked Dynamic", "411": "Ranked", "412": "Ranked", "413": "Ranked", "930": "ARAM", "931": "ARAM", "420": "Ranked Solo/Duo", "421": "Ranked Solo/Duo", "422": "Ranked Solo/Duo", "940": "Nexus Siege", "941": "Nexus Siege", "430": "Normal 5v5 Blind Pick", "431": "Normal", "432": "Normal", "433": "Normal (Blind Pick)", "950": "Doom Bots Voting", "951": "Level 100 Gauntlet", "440": "5v5 Ranked Flex", "441": "Ranked Flex", "442": "Ranked Flex", "960": "Doom Bots Standard", "32": "Co-op vs AI Beginner Bot", "450": "ARAM", "451": "ARAM", "452": "ARAM", "801": "Co-op vs. AI", "970": "Hexakill", "961": "The Teemoing", "460": "Normal 3v3 Blind Pick", "840": "Co-op vs. AI Beginner Bot", "980": "Star Guardian Invasion: Normal", "981": "Star Guardian Invasion: Normal", "470": "Ranked 3v3 Flex", "990": "Star Guardian Invasion: Onslaught", "1000": "PROJECT: Hunters", "1001": "PROJECT: Hunters", "830": "Co-op vs. AI Intro Bot", "1010": "Snow Battle ARURF", "1011": "Snow Battle ARURF", "1200": "Nexus Blitz", "810": "Co-op vs. AI Intro Bot"}


class Queue(Block):
    
    def __init__(self):
        Block.__init__(self, "Queue")
        self.content = {
            "queueId" : Numeric("Queue Id"),
            "queueName" : String("Queue name")
        }
        
    def setValue(self, data):
        self.content["queueId"].setValue(data)
        self.content["queueName"].setValue(queues[str(data)])