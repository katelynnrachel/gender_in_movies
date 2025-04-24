def clean_imdb_data(filepath):
    import pandas as pd

    # Load the dataset
    df = pd.read_csv(filepath)

    # Drop columns you don't need
    df = df[[
        'Series_Title', 'Released_Year', 'Runtime', 'Genre',
        'IMDB_Rating', 'Director', 'Star1', 'Star2', 'Star3', 'No_of_Votes', 'Gross'
    ]]

    # Drop rows with missing information
    df = df.dropna(subset=['Director', 'Star1', 'Gross'])

    # Clean Released_Year (sometimes it's not numeric like 'PG')
    df = df[df['Released_Year'].apply(lambda x: str(x).isdigit())]
    df['Released_Year'] = df['Released_Year'].astype(int)

    # Clean Gross (remove $/commas if needed, then convert to float)
    df['Gross'] = df['Gross'].replace('[\$,]', '', regex=True).astype(float)

    # Extract first names for gender prediction
    df['Director_First'] = df['Director'].apply(lambda x: x.split()[0])
    df['Star1_First'] = df['Star1'].apply(lambda x: x.split()[0] if pd.notnull(x) else None)

    return df
