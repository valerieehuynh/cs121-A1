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



