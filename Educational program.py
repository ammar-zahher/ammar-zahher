import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init(autoreset=True)

G = Fore.GREEN
B = Fore.BLUE
R = Fore.RED
Y = Fore.YELLOW
CY = Fore.CYAN
BR = Style.BRIGHT
RS = Style.RESET_ALL
languge0=input("Which language do you speak?")
languge=languge0.lower().strip()
while True:
    match languge:
        case "english":
            print("Hi,how are you doing\nI hope you are great")
            print("We don`t have a lot of feilds.chose the field that is convinint for you:\n1.learn about Ai.\n2.learn about program\n3.learn about industry.")
            print("chose from(1/3)")
            desire=input("What do you want to learn?")
            match desire:
                case "1":
                    print("absolutely take.")
                    try:
                        socket=urllib.request.urlopen("https://www.ibm.com/think/topics/artificial-intelligence")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------artificial intelligence (AI)------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("Do you like it?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="yes":
                            print("Thank you.")
                            continue
                        elif Satisfaction=="no":
                            try:
                                socket=urllib.request.urlopen("https://www.coursera.org/articles/what-is-artificial-intelligence")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------What Is Artificial Intelligence------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("Do you like it?I hope you like it.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="yes":
                                    print("ok.that is great.")
                                    continue
                                elif Satisfaction_1=="no":
                                    print("try this.")
                                    try:
                                        socket=urllib.request.urlopen("https://cloud.google.com/learn/what-is-artificial-intelligence")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------a simple-to-understand guide------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                                              print("There is a small problem, please check your connection...")
                                                              continue
                            except:
                                              print("There is a small problem, please check your connection...")
                                              continue
                    except:
                        print("There is a small problem, please check your connection...")
                        continue
                case "2":
                    print("absolutely take.")
                    try:
                        socket=urllib.request.urlopen("https://www.freecodecamp.org/news/how-to-learn-programming/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------How to Learn Programming------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("Do you like it?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="yes":
                            print("Thank you.")
                            continue
                        elif Satisfaction=="no":
                            try:
                                socket=urllib.request.urlopen("https://www.python.org/about/gettingstarted/")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------Python For Beginners------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("Do you like it?I hope you like it.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="yes":
                                    print("ok.that is great.")
                                    continue
                                elif Satisfaction_1=="no":
                                    print("try this.")
                                    try:
                                        socket=urllib.request.urlopen("https://realpython.com/documenting-python-code/")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------Documenting Python Code------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                    except:
                                                      print("There is a small problem, please check your connection...")
                                                      continue
                            except:
                                              print("There is a small problem, please check your connection...")
                                              continue
                    except:
                        print("There is a small problem, please check your connection...")
                        continue
                case "3":
                    print("absolutely take.")
                    try:
                        socket=urllib.request.urlopen("https://umbrex.com/resources/how-industries-work/automotive-transportation/how-the-automotive-manufacturers-oems-industry-works/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------How the Automotive Manufacturing Industry Works------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("Do you like it?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="yes":
                            print("Thank you.")
                            continue
                        elif Satisfaction=="no":
                            try:
                                socket=urllib.request.urlopen("https://www.mrpeasy.com/blog/manufacturing/")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------The Ultimate Introduction to Manufacturing (2026)------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("Do you like it?I hope you like it.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="yes":
                                    print("ok.that is great.")
                                    continue
                                elif Satisfaction_1=="no":
                                    print("try this.")
                                    try:
                                        socket=urllib.request.urlopen("https://industrytoday.com/2026-4-key-trends-in-manufacturing-and-auto/")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------4 Key Trends in Manufacturing and Auto------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                        print("There is a small problem, please check your connection...")
                                        continue
                            except:
                                print("There is a small problem, please check your connection...")
                                continue
                    except:
                        print("There is a small problem, please check your connection...")
                        continue
                case _:
                    print("I am sory we don`t know what do you mean?")
        case "arabic":
            print("مرحبا,كيف حالك اتمنى ان تكون بخير")
            print("نحن لا نمتلك العديد من المجالات.اختر المجال المناسب لك:\n1.تعلم عن الذكاء الاصطنعي.\n2.تعلم عن البرمجة\n3.تعلم عن الصناعة")
            print("اختر من(1/3)")
            desire=input("ماذا تريد ان تتعلم?")
            match desire:
                case "1":
                    print("بلطبع,خذ.")
                    try:
                        socket=urllib.request.urlopen("https://mawdoo3.com/%D8%AA%D8%B9%D8%B1%D9%8A%D9%81_%D8%A7%D9%84%D8%B0%D9%83%D8%A7%D8%A1_%D8%A7%D9%84%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------تعريف الذكاء الاصطناعي------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("هل اعجبك?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="نعم":
                            print("شكرا لك.")
                            continue
                        elif Satisfaction=="لا":
                            try:
                                socket=urllib.request.urlopen("https://mawdoo3.com/%D8%B9%D9%84%D8%A7%D9%82%D8%A9_%D8%A7%D9%84%D8%B0%D9%83%D8%A7%D8%A1_%D8%A7%D9%84%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A_%D8%A8%D9%85%D8%B3%D8%AA%D9%82%D8%A8%D9%84_%D8%A7%D9%84%D9%88%D8%B8%D8%A7%D8%A6%D9%81")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------علاقة الذكاء الاصطناعي بمستقبل الوظائف------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("هل اعجبك ذالك,أمل ان يعجبك")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="نعم":
                                    print("حسنا.ذالك جيد")
                                    continue
                                elif Satisfaction_1=="no":
                                    print("جرب هاذا.")
                                    try:
                                        socket=urllib.request.urlopen("https://tech.mawdoo3.com/b/%D8%A3%D9%86%D9%88%D8%A7%D8%B9-%D8%A7%D9%84%D8%B0%D9%83%D8%A7%D8%A1-%D8%A7%D9%84%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------أنواع الذكاء الاصطناعي------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                        print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                        continue
                            except:
                                print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                continue
                    except:
                        print("نحن لا نعرف مايعني هاذا\nاعد المحولة")
                        continue
                case "2":
                    print("absolutely take.")
                    try:
                        socket=urllib.request.urlopen("https://academy.hsoub.com/programming/general/%D8%A3%D9%87%D9%85%D9%8A%D8%A9-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-%D8%A3%D9%87%D9%85-%D9%84%D8%BA%D8%A7%D8%AA-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------أهمية البرمجة وأهم لغات البرمجة------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("هل اعجبك ذالك?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="نعم":
                            print("شكرا لك.")
                            continue
                        elif Satisfaction=="لا":
                            try:
                                socket=urllib.request.urlopen("https://tech.mawdoo3.com/b/%D8%A3%D9%87%D9%85%D9%8A%D8%A9-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------أهمية البرمجة في الحياة------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("هل اعجبك ذالك?اتمنى ان يعجبك.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="نعم":
                                    print("حسنا.ذالك جيد")
                                    continue
                                elif Satisfaction_1=="لا":
                                    print("جرب هاذا.")
                                    try:
                                        socket=urllib.request.urlopen("https://tech.mawdoo3.com/b/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%D8%A7%D8%AA-%D9%84%D8%BA%D8%A7%D8%AA-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------استخدامات لغات البرمجة------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                    except:
                                        print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                        continue
                            except:
                                print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                continue
                    except:
                        print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                        continue
                case "3":
                    print("طبعا خذ.")
                    try:
                        socket=urllib.request.urlopen("https://www.almuraba.net/%d8%aa%d8%b5%d9%86%d9%8a%d8%b9-%d8%a7%d9%84%d8%b3%d9%8a%d8%a7%d8%b1%d8%a9/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------كيف تُصنع السيارات؟------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("هل اعجبك ذالك?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="نعم":
                            print("Thank you.")
                            continue
                        elif Satisfaction=="لا":
                            try:
                                socket=urllib.request.urlopen("https://mawdoo3.com/%D9%85%D9%81%D9%87%D9%88%D9%85_%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D8%A9_%D9%88%D8%AA%D8%B7%D9%88%D8%B1%D9%87%D8%A7")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------مفهوم الصناعة وتطورها------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("هل اعجبك هاذا؟اتمنى ان يعجبك.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="نعم":
                                    print("حسنا.ذالك جيد")
                                    continue
                                elif Satisfaction_1=="لا":
                                    print("جرب هاذا.")
                                    try:
                                        socket=urllib.request.urlopen("https://mawdoo3.com/%D8%A8%D8%AD%D8%AB_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D8%A9")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------بحث عن الصناعة------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                        print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                        continue
                            except:
                                print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                                continue
                    except:
                        print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
                        continue
                case _:
                    print("هناك مشكلة صغيرة, من فضلك تاكد من اتصالك...")
        case "汉语":       
            print("嗨,你好吗\n我希望你很棒")
            print("我们的田地不多.选择自己方便的领域:\n1.了解人工智能.\n2.了解程序\n3.了解行业.")
            print("选择 (1/3)")
            desire=input("你想学什么?")
            match desire:
                case "1":
                    print("绝对采取.")
                    try:
                        socket=urllib.request.urlopen("https://aws.amazon.com/cn/what-is/artificial-intelligence/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------什么是人工智能（AI)------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("你喜欢吗?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="是的":
                            print("谢谢.")
                            continue
                        elif Satisfaction=="否":
                            try:
                                socket=urllib.request.urlopen("https://cloud.google.com/learn/what-is-artificial-intelligence?hl=zh-cn")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------人工智能 (AI)：简明指南------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("你喜欢吗? 希望你喜欢它。.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="是的":
                                    print("好的。 这很好.")
                                    continue
                                elif Satisfaction_1=="否":
                                    print("试试这个.")
                                    try:
                                        socket=urllib.request.urlopen("https://quanshugu.com/hefwdq/zhineng/g74616.html")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------關於人工智慧作文集合十篇------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                        print("有一个小问题,请检查你的连接......")
                                        continue
                            except:
                                print("有一个小问题,请检查你的连接......")
                                continue
                    except:
                        print("有一个小问题,请检查你的连接......")
                        continue
                case "2":
                    print("绝对采取.")
                    try:
                        socket=urllib.request.urlopen("https://wptoolbear.com/%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------程式設計高效學習指南------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("你喜欢吗?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="是的":
                            print("谢谢.")
                            continue
                        elif Satisfaction=="否":
                            try:
                                socket=urllib.request.urlopen("https://www.edntaiwan.com/20240618nt61-where-should-you-put-the/")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------寫程式時把「{」放在單獨一行還是同一行好？------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("你喜欢吗?希望你喜欢它.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="是的":
                                    print("好的。 这很好.")
                                    continue
                                elif Satisfaction_1=="否":
                                    print("试试这个.")
                                    try:
                                        socket=urllib.request.urlopen("https://informatecdigital.com/zh-TW/%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E5%9F%BA%E7%A4%8E-%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5/")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------程式設計基礎：基本概念------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                    except:
                                        print("有一个小问题,请检查你的连接......")
                                        continue
                            except:
                                print("有一个小问题,请检查你的连接......")
                                continue
                    except:
                        print("有一个小问题,请检查你的连接......")
                        continue
                case "3":
                    print("绝对采取.")
                    try:
                        socket=urllib.request.urlopen("https://www.wonderfulpcb.com/zh-TW/blog/industrial-application-development-modern-manufacturing/")
                        reader=socket.read()
                        case_1_url=BeautifulSoup(reader,"html.parser")
                        case_1_url=case_1_url.get_text()
                        print("------工業應用開發對現代製造業的重要性------\n")
                        for line in case_1_url.splitlines():
                            if line.strip():
                                print(line.strip())
                        Satisfaction0=input("你喜欢吗?")
                        Satisfaction=Satisfaction0.lower()
                        if Satisfaction =="是的":
                            print("谢谢.")
                            continue
                        elif Satisfaction=="否":
                            try:
                                socket=urllib.request.urlopen("https://balabibi.com/%E5%B7%A5%E6%A5%AD%E7%99%BC%E5%B1%95%E7%9A%84%E8%9B%BB%E8%AE%8A%E3%80%81%E5%89%B5%E6%96%B0%E5%92%8C%E5%89%8D%E6%99%AF%EF%BC%81%E6%9C%AA%E4%BE%86%E5%A6%82%E4%BD%95%E6%94%B9%E8%AE%8A%EF%BC%9F/")
                                reader=socket.read()
                                case_1_url=BeautifulSoup(reader,"html.parser")
                                case_1_url=case_1_url.get_text()
                                print("------工業發展的蛻變、創新和前景！未來如何改變？------\n")
                                for line in case_1_url.splitlines():
                                    if line.strip():
                                        print(line.strip())
                                Satisfaction_7=input("你喜欢吗? 希望你喜欢它。.")
                                Satisfaction_1 =Satisfaction_7.lower()
                                if Satisfaction_1=="是的":
                                    print("好的。 这很好.")
                                    continue
                                elif Satisfaction_1=="否":
                                    print("试试这个。")
                                    try:
                                        socket=urllib.request.urlopen("https://www.nopss.gov.cn/BIG5/n1/2022/0616/c219544-32448015.html")
                                        reader=socket.read()
                                        case_1_url=BeautifulSoup(reader,"html.parser")
                                        case_1_url=case_1_url.get_text()
                                        print("------龍海波 華若筠：工業現代化的戰略使命與發展邏輯------\n")
                                        for line in case_1_url.splitlines():
                                            if line.strip():
                                                print(line.strip())
                                                continue
                                    except:
                                        print("有一个小问题,请检查你的连接......")
                                        continue
                            except:
                                print("有一个小问题,请检查你的连接......")
                                continue
                    except:
                        print("有一个小问题,请检查你的连接......")
                        continue
                case _:
                    print("对不起,我们不知道你的意思。")
        case _:
            print("we don`t have this languge.")
            print("we have just three language\n1.english\n2.arabic\n3.汉语")
            break
