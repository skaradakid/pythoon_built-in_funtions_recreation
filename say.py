def say(*values: object, sep: str = ' ', end: str = '\n', file: IO = "file.txt"):
    """this function is made to do thee same thing as the print function"""
    if file:
        with open(file, 'w') as f:
            sys.stdout = f  
            for value in values:
                f.write(f"{value}{sep}")
            f.write(end)
        f.close()
        
    else:
        for value in values:
            sys.stdout.write(f"{value}{sep}")
        sys.stdout.write(end)
