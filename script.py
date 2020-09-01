import csv
from PIL import Image, ImageDraw, ImageFont
def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width)
def coupons(names: list, certificate: str, font_path: str):
    textcolor ='000'
    for name in names:

        # opens the image
        img = Image.open(certificate, mode ='r')
        draw = ImageDraw.Draw(img)
        default_font_size= 25
        font = ImageFont.truetype(font_path, default_font_size)
        min_cordinate= 563
        max_cordinate=773
        x=563
        y=663
        text = name[1]
        #Adjusting the size
        while x+get_text_dimensions(text,font)<max_cordinate:
            if abs(abs(x-min_cordinate)-abs(max_cordinate-(x+get_text_dimensions(text,font))))<=2:
                break
            x+=1
        while x+get_text_dimensions(text,font)>max_cordinate-75:
            if abs(abs(x-min_cordinate)-abs(max_cordinate-(x+get_text_dimensions(text,font))))<=2:
                break
            default_font_size=max(12,default_font_size-1)
            x+=1
            y+=1
            font=ImageFont.truetype(font_path,default_font_size)

        # drawing text size
        #The city name

        draw.text((x,y), text, fill="black",font = font, align ="center")
        #Squad
        default_font_size= 25
        font = ImageFont.truetype(font_path, default_font_size)
        text=name[2];
        draw.text((878,663), text, fill="black",font = font, align ="center")
        #Gender
        text=name[3]
        draw.text((820,628), text, fill="black",font = font, align ="center")
        #Name
        default_font_size=40
        text=name[0]
        font = ImageFont.truetype(font_path, default_font_size)
        x=img.size
        draw.text(((x[0]-get_text_dimensions(text,font))/2, 560),text, fill="black", font= font, align="center")
        # saves the image in png format
        img.save("{}.png".format(name))
filename = "data.csv"
fields= []
rows = []
with open(filename , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

if __name__=="__main__":
    FONT="../fonts/Arial Rounded Bold.ttf"
    CERTIFICATE= "Template1.jpg"
    coupons(rows,CERTIFICATE,FONT)
