

def main():
    
    bestand = ""
    h = 0
    
    print ("DdeI\nBspMII\nEcoRI\nHindIII\nBalI \nSmaI\nSwaI\nAciI\nSspI\nXhoI\nAvrII\nApaLI\nTaqI\nEcoRV\nFictIe\nFictII\n")
    enzym = input("Kies een restrictie enzym uit de lijst hier boven: ")
    hoeveel = int(input("Geef aan hoeveel sequenties uit het bestand je wilt checken: "))
    print ("Dit kan even duren...")
    try:
        headers, seqs = lees_inhoud()
        
        for element in seqs[0:hoeveel]:
            h +=1
            print (40* "=")
            print ("Header:\n", headers[h], "\n")
            print ("Sequentie:\n",element,"\n")
            print ("Deze sequentie is DNA: ",is_dna(element))
            knipt (element, hoeveel, enzym)
            print ("\n")
        print (40* "=")

    except FileNotFoundError:
        print ("\nEr is geen bestand aanwezig. Voeg een bestand toe waaruit het programma de data kan halen. Deze MOET in .fna format zijn")
    
#   zoekwoord = input("Geef een zoekwoord op: ")


    
    
def lees_inhoud():

    
        bestand = open('alpaca.fna',"r")
        headers = []
        seqs = []
        seq  = ""

        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
            seqs.append(seq)
     
        return headers, seqs
    


    
def is_dna(element):
    
    x = ""
    
    for c in element:
        
        if c == "A" or "T" or "G" or "C":
            x = "true"
    if x != "true":
        x = "false"

    return x
    


def knipt(element, hoeveel, enzym):

    global y
   
    naam=[]
    begin = []
    eind = []
    sublijst=[]
    x = 0
    restenz = ""
    sequentie = ""
    hoeveel += 1
    y = 0

    print ("element", element)
    print ("enzym", enzym)

    bestand = open("enzymen.txt")
    for line in bestand:
        enzym_a = line
        name, sequence = enzym_a.split (' ') 
        naam.append(name)
        beg, end= sequence.split('^')
        begin.append(beg)
        eind.append(end)
        
    
    sequentie = element
            
    for element in naam:
        if enzym == element:
            
                   
                print ("\nNaam enzym:            ",element)
                print ("Sequentie enzym:       ",begin[x],eind[x])
            

                

                if begin[x] and eind[x] in sequentie:
                    y = 1
                    print ("Dit restrictie enzym bevind zich in de sequentie")
                else:
                    y = 0
                    print ("Dit restrictie enzym bevind zich niet in de sequentie")
                x +=1
           
        x = 0

    
main()
