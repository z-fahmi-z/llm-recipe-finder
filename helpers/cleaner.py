import pandas as pd
pd.options.mode.copy_on_write = True

def clean_missing(df):
    return df[(
        - df["Ingredients"].isna() &
        - df["Steps"].isna()
        )]

def clean_title_dupes(df):
   df["Title"] = (df["Title"]
                  .str.title()
                  .str.replace(r"^[^a-zA-Z]*", "", regex=True))
   count_title = df["Title"].value_counts().reset_index().sort_values("count", ascending=False)
   df_title_dupes = count_title[
    count_title["count"] > 1
   ]
   df_unique = df[
    ~df["Title"].isin(df_title_dupes["Title"])
   ]
   df_dupes = df[
    df["Title"].isin(df_title_dupes["Title"])
   ]
   max_df_dupe_loves = df_dupes.loc[
    df_dupes.groupby("Title")["Loves"].idxmax()
   ]
   return pd.concat([
    max_df_dupe_loves,
    df_unique
    ]).reset_index(drop=True)