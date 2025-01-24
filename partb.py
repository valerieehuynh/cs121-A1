import sys

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

def common_words(file1_path, file2_path):
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