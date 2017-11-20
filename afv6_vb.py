# Naam:

# Datum:
# Versie:

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    
    try:
        bestand = "alpaca_test.fa"
        headers, seqs = lees_inhoud(bestand)
    
        
     
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:",headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
    except FileNotFoundError:
        print ("Er is geen bestand aanwezig. Voeg een bestand toe waaruit het programma de data kan halen. Deze MOET in .FASTA format zijn")
    except UnicodeDecodeError:
        print ("Dit bestand is geen .FASTA bestand. Voer een .FASTA bestand in, in de map.")
    #except Exception:
        print ("Het programma geeft geen Boolean waarde")
    except TypeError:
        print ("Het programma heeft niet de verwachte input en kan het dus niet verwerken. Kijk of het bestand volledig is.")
def lees_inhoud(bestands_naam):
      
     bestand = open(bestands_naam)
     headers = []
     seqs = []
     seq = ""
     for line in bestand:
         line=line.strip()
         if ">" in line:
             if seq != "":
                 seqs.append(seq)
                 seq = ""
             headers.append(line)
         else:
             seq += line.strip()
     seqs.append(seq)
     return headers, seqs

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    #if dna != True or False:
        #raise Exception
            
    return dna

# bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^","")


        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a + t + c + g
        if total != len(seq):
            raise TypeError

        a = alpaca_seq.count("A")
        t = alpaca_seq.count("T")
        c = alpaca_seq.count("C")
        g = alpaca_seq.count("G")
        total = a + t + c + g
        if total != len(alpaca_seq):
            raise TypeError

        
        
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
    
    


main()
