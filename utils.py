# TODO: Update the get_distribution_dict with the latest greatest version when done
def get_distribution_dict(dat, filter_ys = None):
    """filter is None or a list of years"""
    qavals_dict = {'continuous':{}, 'cat':{}}
    qavals_dict['continuous'] 

    # Temp: Check distribution of vars
    if filter_ys != None:# If there's a filter     
        dat = dat[dat['issue_year'].isin(filter_ys)]
        
    tempqa = dat[lists.continuous_cols_4_model].describe()
    for col in tempqa.columns:
        qavals_dict['continuous'][col] = {}

    for col in tempqa.columns:
        qavals_dict['continuous'][col]['min'] = tempqa[tempqa.index=='min'][col].values[0]
        qavals_dict['continuous'][col]['max'] = tempqa[tempqa.index=='max'][col].values[0]
    return qavals_dict