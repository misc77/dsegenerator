from docx import Document

""" 
    readTable

    reads the content of a word table
    and puts the content into an instance of checklist class.
    This instance will be persisted into an Sqlite table
"""
def readTable(table):
    r = c = 0
    print("columns: " + str(len(table.columns)) + " rows: " + str(len(table.rows)))

    for row in table.rows:
        r=r+1
        print("---- row " + str(r) + "---")
        c=0
        for col in table.columns:
            c=c+1
            cell = table.cell(r-1, c-1)
            print(str(r) +"," + str(c))
            print(cell.text)
            if len(cell.tables) > 0:
                for t in cell.tables:
                    readTable(t)

"""
    readChecklist

    reads the input document that is basis for
    generation of the dse-document
"""
def readChecklist(file):
    document = Document(file)
    i = 0

    for t in document.tables:
        i=i+1
        print("####### START (" + str(i) + ") #######")
        readTable(t)
        print("####### END (" + str(i) + ") #######")
        print("")
        if i>=5:
            break

    print("document finished - contained " + str(i) + " tables")


readChecklist("C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.docx")