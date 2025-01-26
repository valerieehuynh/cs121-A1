import sys

"""
runs in linear complexity O(n). iterates through all characters in file once. 
"""
def tokenize(file):
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
runs in O(n1+n2). find common words between two files. n1 & n2 are total characters in file1 & file2. 
tokenizing them is O(n). 
"""
def common_words(file1_path, file2_path):
    """
    runs in O(n1 + n2). computes number of common words through processing two input files. 
    """
    t1 = set(tokenize(file1_path))
    t2 = set(tokenize(file2_path))


    common_words = t1.intersection(t2)

    return len(common_words)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Error. Use it like this: python PartB.py TextFilePath1 TextFilePath2")
        sys.exit(1)

    f1 = sys.argv[1]
    f2 = sys.argv[2]

    try:
        
        result = common_words(f1, f2)

        
        print(result)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    except FileNotFoundError as e:
        print(f"File not Found: {e}")
        sys.exit(1)