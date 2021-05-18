import pandas as pd

# snippet data
data = [
{"id": 4526, "source": 1, "status": 2, "priority": 1, "subject": "Re: Company A - Application Successfully Submitted"},
{"id": 4527, "source": 9, "status": 2, "priority": 4, "subject": "Assessment is not working"},
{"id": 4528, "source": 2, "status": 4, "priority": 1, "subject": "Network disconnect"},
{"id": 4529, "source": 1, "status": 3, "priority": 3, "subject": "Company B - Login failure"},
]

# replace value code to value name
def transform_integer_to_string(d):
    df = pd.DataFrame.from_dict(d)

    # variable name
    source_code = [1,2,3,7,8,9]
    source_name = ['email','portal','phone','chat','mobile','feedback_widget']
    status_code = [2,3,4,5]
    status_name = ['open','pending','resolved','closed']
    priority_code = [1,2,3,4]
    priority_name = ['low','medium','high','urgent']

    df['source'] = df['source'].replace(source_code, source_name)
    df['status'] = df['status'].replace(status_code, status_name)
    df['priority'] = df['priority'].replace(priority_code, priority_name)

    df_dict = df.to_dict('records')

    return df_dict

def main():
    transform_data = transform_integer_to_string(data)
    print(transform_data)

if __name__ == "__main__":
    main()