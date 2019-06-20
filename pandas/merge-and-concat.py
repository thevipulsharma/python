import pandas as pd

t_list = [
    ["a", "c", 1],
    ["a", "e", 2],
    ["b", "d", 3],
    ["c", "e", 4],
    ["a", "g", 10],
    ["d", "f", 11],
    ["d", "g", 12]       
]

u_list = [
    ["a", "e", 5],
    ["b", "d", 6],
    ["d", "g", 13]        
]

k_list = [
    ["a", 7],
    ["b", 8],
    ["e", 9]
]

t_df = pd.DataFrame(t_list, columns = ["word-1", "word-2", "score"])
u_df = pd.DataFrame(u_list, columns = ["word-1", "word-2", "score"])
k_df = pd.DataFrame(k_list, columns = ["word", "score"])

# Primary DataFrame
p_df_1 = pd.merge(k_df[["word"]], u_df, how="inner", left_on="word", right_on="word-1")
p_df_1 = p_df_1[["word", "word-2", "score"]]
p_df_1.columns = ["keyword", "word", "score"]

p_df_2 = pd.merge(k_df[["word"]], u_df, how="inner", left_on="word", right_on="word-2")
p_df_2 = p_df_2[["word", "word-1", "score"]]
p_df_2.columns = ["keyword", "word", "score"]

p_df = pd.concat([p_df_1, p_df_2], ignore_index=True)

# Secondary DataFrame
s_df_1 = pd.merge(k_df[["word"]], t_df, how="inner", left_on="word", right_on="word-1")
s_df_1 = s_df_1[["word", "word-2", "score"]]
s_df_1.columns = ["keyword", "word", "score"]

s_df_2 = pd.merge(k_df[["word"]], t_df, how="inner", left_on="word", right_on="word-2")
s_df_2 = s_df_2[["word", "word-1", "score"]]
s_df_2.columns = ["keyword", "word", "score"]

s_df = pd.concat([s_df_1, s_df_2], ignore_index=True)
s_df = pd.merge(s_df, p_df, how="left", on=["keyword", "word"], indicator=True)
s_df = s_df[s_df["_merge"] != "both"]
s_df = s_df[["keyword", "word", "score_x"]]
s_df.columns = ["keyword", "word", "score"]

p_dict = p_df.to_dict(orient="records")
s_dict = s_df.to_dict(orient="records")
