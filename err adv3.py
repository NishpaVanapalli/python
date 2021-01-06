##import fpdf
##pdf=fpdf.FPDF()
##pdf.add_page()
##pdf.out("out.pdf")


##for i in range(10):
##    pdf.add_page("L")
##    pdf.image("certi.jpg",0,0,297,200)
##pdf.output("out.pdf")


##import fpdf
##import csv
##pdf=fpdf.FPDF()
##data=[]
##with open("2023.csv") as file1:
##    records=list(csv.reader(file1))
##    for record in records:
##        data.append(record)
##print(len(data))
##for i in range(len(data)):
##    pdf.add_page("L")
##    pdf.image("certi.jpg",0,0,297,200)
##    pdf.set_front("Times"," ", 20)
##    pdf.set_xy(120,280)
##    pdf.cell(0,0,data[i][2])
##pdf.output("out.pdf")
