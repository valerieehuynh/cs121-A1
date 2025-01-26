import sys

def tokenize(file):
    """
    runs in linear complexity O(n). iterates through all characters in file. 
    """
    result = []

    try:
        with open(file, 'r', encoding='utf-8') as f:

            for i in f:
                
                temp = ""

                for j in i:

                    if j.isalnum(): 
                        temp = temp + j.lower()

                    elif temp:  
                        result.append(temp)
                        temp = ""

                if temp:  
                    result.append(temp)

    except Exception as e:
        print(f"Can't read file: {e}")
        sys.exit(1)
    
    except UnicodeDecodeError:
        print("Can't decode this file.")
        sys.exit(1)

    except FileNotFoundError:
        print(f"File not Found: {file}")
        sys.exit(1)
    
    
    return result

    """
    m = tokens
    runs in O(m). iterates through tokens and checks if it exists. if it does then it updates count. 
    """
def compute_word_frequencies(tokens):
    result = {}

    for i in tokens:

        if i not in result:
            result[i] = 1
            
        else:
            result[i] = result[i] + 1
            
    return result

    """
    runs in O(k log k). runtime grows to input of k. it sorts and prints frequencies in descending order
    and lexigraphocally. k = unique # of words.
    """

def print_frequencies(frequencies):
    freqs = []

    for k, v in frequencies.items(): 
        freqs.append((k, v))

    
    def sort_key(item):

        return (-item[1], item[0])  

    sortedFreqs = sorted(freqs, key=sort_key)

    
    for k, v in sortedFreqs:
        print(f"{k}\t{v}")

    """
    runs in O(n + m + k log k).  n = # of characters in file, m = # of tokens, k = # of uniqiue words
    """
if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Error. Use it like this: python PartA.py TextFilePath")
        sys.exit(1)

    filePath = sys.argv[1]

    try:
        
        tokens = tokenize(filePath)
        words = compute_word_frequencies(tokens)
        print_frequencies(words)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


    except FileNotFoundError:
        print(f"Error: The file path isn't valid or DNE: '{filePath}'.")
        sys.exit(1)

