import numpy as np

def calculate_batches(df, wanted_rows_per_batch, print_process=False):
    batches_created = int(len(df) / wanted_rows_per_batch)
    if print_process:
        print(f"""
        Dataframe length: {len(df)}
        Wanted rows per batch: {wanted_rows_per_batch}
        Batches created: {batches_created}
        """)
    return batches_created

def batch_dataframe(df_subset_as_list, batches_number):
    return np.array_split(df_subset_as_list, batches_number)