import gspread
from oauth2client.service_account import ServiceAccountCredentials




class GooWorkbook:
    scopes = ['https://spreadsheets.google.com/feeds',
              'https://www.googleapis.com/auth/drive',]
    
    def __init__(self, workbook_title, *, oauth2Keys='client_secret.json'):
        self.workbook_title = workbook_title
        
        self.credentials = self.oauth2_credentials(oauth2Keys)
        self.client = self.client_init()
        self.workbook = self.get_workbook(workbook_title)

        self.sheets = self.workbook_sheets()

    def __enter__(self):
        print('Workbook "{}":\n\n\t{}\n\n{}'.format(self.workbook_title, '\n\t'.join(self.sheets), '-'*70))
        return self.workbook, self.sheets

    def __exit__(self, exc_class, exc_msg, exc_trace):
        print('-'*70, '\nClosing workbook: {}'.format(self.workbook_title))
        pass
    
    def oauth2_credentials(self, oauth2Keys):
        return ServiceAccountCredentials.from_json_keyfile_name(oauth2Keys, self.scopes)

    def client_init(self):
        return gspread.authorize(self.credentials)

    def get_workbook(self, title):
        return self.client.open(title)

    def workbook_sheets(self) -> dict:
        return {i.title: i for i in self.workbook.worksheets()}
        


if __name__ == '__main__':
    with GooWorkbook('aa1a') as (workbook, sheets):
        sheet1 = sheets['Соленья']
        for i in sheet1.get_all_records():
            print(i, end='\n\n')

        for title in sheets:
            if title == 'МазикS':
                sheet = sheets[title]
                
                cell_list1 = sheet.range('A2:G7')
                cell_list2 = sheet1.range('A2:G7')

                print(cell_list1)
                print(cell_list2)
                [setattr(o, 'value', str(v.value.strip()[:-1].upper() + v.value.strip()[-1].lower())[::-1]) for o, v in zip(cell_list1, cell_list2) if v.value]
                sheet.update_cells(cell_list1)


        from random import choice
        for title in sheets:
            if title == 'Мазик':
                sheet = sheets[title]
                
                cell_list = sheet.range('A2:G50000')

                
                
                for i, o in enumerate(cell_list):
                    o.value = i

                letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

                #cell_list = (cell_list[i:i + len(letters)] for i in range(0, len(cell_list), len(letters)))
                    
                
                for n, L in enumerate(letters):
                    

                    for o in (cell_list[i:i + len(letters)] for i in range(0, len(cell_list), len(letters))):

                        if L == 'F':
                            o[n].value = float('{}.{}'.format(choice(range(0, 2000)), choice(range(0, 10))))
                            
                        elif L == 'C':
                            o[n].value = choice(['мазик классический', 'мазик оливковый', 'мазик c вишней', 'мазик чесночный', 'соленая сметана'])

                        elif L == 'B':
                            o[n].value = choice(['мазик'])

                        elif L == 'G':
                            o[n].value = 'https://pic.com/{}'.format(choice(range(50000)))
                        elif L == 'A':
                            o[n].value = choice(['Сибирский мазик', 'Мазик бутик', 'Мазик Бабаевский', 'Веселый мазик', 'Простомазик', 'MAZIKOFF'])

                        elif L == 'E':
                            o[n].value = choice(['стекло', 'пластик', 'пакет'])
                        elif L == 'D':
                            o[n].value = choice(range(0, 3000, 10))

                            
                        else:
                            o[n].value = L + ' изи мазик ' + str(o[n].value)

                        
                        
                
                
                sheet.update_cells(cell_list)
        """
        from data import test_data
        for title in sheets:
            
            if title == 'Сгущенка':
                sheet = sheets[title]

                cell_list2 = []
                rows = 1
                for item in test_data['молочная косервация']:
                    for key in item:
                        rows += 1
                        t, n, w, i = item[key].values()
                        cell_list2.extend([t, '', n, int(w), '', '', i])
                
                    
                cell_list1 = sheet.range('A2:G{}'.format(rows))


                [setattr(o, 'value', v) for o, v in zip(cell_list1, cell_list2) if v]
                sheet.update_cells(cell_list1)
        """
            


"""
client = gspread.authorize(creds)
sheet = client.open('aa1a').sheet1
tabula = sheet.get_all_records()

print(tabula)
#sheet.update_cell(1, 1, 'BUAGGAGAGAG')
#print(tabula)


row = ['#################', '123123', 5.77, 5666, 'spam']
##for i in range(5, 1000):
##    sleep(1)
##    sheet.insert_row([i] + row, i)

cell_list = sheet.range('A1:A700')

# Update values
for cell in cell_list:
    cell.value = "Hello_World"

# Send update in batch mode
sheet.update_cells(cell_list)

cell_list = sheet.range('B1:B700')

# Update values
for cell in cell_list:
    cell.value = "12333"

# Send update in batch mode
sheet.update_cells(cell_list)


sheet.update_cells(cell_list)

cell_list = sheet.range('C1:C700')

# Update values
for cell in cell_list:
    cell.value = "Detalite"

# Send update in batch mode
sheet.update_cells(cell_list)
"""
