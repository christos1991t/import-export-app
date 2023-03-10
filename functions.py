import pandas as pd
import io
import zipfile


def import_klant(file1_path):
    client_export = pd.read_excel(file1_path)
    return client_export


def submit_columns(idon, idog, file1_path):
    path_step_3 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%203%20import.xlsx'
    path_step_6 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%206%20import.xlsx'
    path_step_7 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%207%20import.xlsx'
    path_step_8 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%208%20import.xlsx'

    Step_3_Import = pd.read_excel(path_step_3)
    Step_6_Import = pd.read_excel(path_step_6)
    Step_7_Import = pd.read_excel(path_step_7)
    Step_8_Import = pd.read_excel(path_step_8)

    if idon != '' and idog != '':
        Step_8_Import.loc[:, 'Eis ID ON'] = Step_7_Import.loc[:, 'Eis ID ON'] = \
            Step_6_Import.loc[:, 'Eis ID ON'] = Step_3_Import.loc[:, 'ID ON'] = import_klant(file1_path).loc[:, idon]
        Step_8_Import.loc[:, 'Eis ID OG'] = Step_7_Import.loc[:, 'Eis ID OG'] = \
            Step_6_Import.loc[:, 'Eis ID OG'] = Step_3_Import.loc[:, 'ID OG'] = import_klant(file1_path).loc[:, idog]
    else:
        pass

    return Step_3_Import, Step_6_Import, Step_7_Import, Step_8_Import


def imports_maken(df1, df2):
    with io.BytesIO() as output:
        with zipfile.ZipFile(output, mode="w") as zip_file:
            df1.to_excel("Step 3 Import.xlsx", index=False)
            df2.to_excel("Step 6 Import.xlsx", index=False)
            zip_file.write("Step 3 Import.xlsx")
            zip_file.write("Step 6 Import.xlsx")
        zip_contents = output.getvalue()
    return zip_contents

