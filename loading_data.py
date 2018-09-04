class structure_data:
    import pandas as pd

    # =============================================================================
    # filepath = "enron.txt"
    # with open(filepath) as fp:
    #     for count, line in enumerate(fp):
    #         line = list(map(int,line.split(" ")))
    #         line = pd.Series(line)
    #         df = df.append(line,ignore_index = True)
    #         print count
    # df.columns = ['DocumentID', 'WordID', 'WordCount']
    # df.to_csv('word_data.csv')
    # =============================================================================
    
    df = pd.read_csv('UCI_data/word_data.csv')
    del df["Unnamed: 0"]
    