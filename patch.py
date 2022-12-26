import os
class lshook:
    def __init__(self,apk,level):
        self.apk =apk
        self.level =level
    def hook(self):
        print("Hooking...........")
        os.system(f"java -jar lspatch.jar --sigbypasslv {self.level} {self.apk}")
        
    def help(self):
        pass
        
class ken:
    def __init__(self,embed,apk):
        self.embed = embed
        self.apk = apk
    def embed_modules(self):
        os.system(f"java -jar lspatch.jar --embed {self.embed} {self.apk}")
        
        
print("\t\n----------------:::::::LSPATCH AUTOMATION BY @KEN:::::::::------------")
apk_name = input("Enter the apllication name with {name}.apk:")
if apk_name=="":
    print("\t\n.......Enter the app name to hook!...")
    exit()
else:
    print(f"\n\nwhat do you want to hook in {apk_name}")
    print("\n\t\n---------MENU TO HOOK-----------:\n\n")
    print("\t1. Signature bypass\n\t2. embed xposed modules to target apk (no-root)\n3. about lspatch")
    choice = int(input("Your choice (1,2 or3)"))
    if choice==1:
        level_bypass= int(input("Enter the level to bypass hint(0,1 or 2):"))
        my_patch =lshook(apk_name,level_bypass)
        print("\n\nHooking…..…..…..………\n\n")
        my_patch.hook()
        
    elif choice==2:
        module = input("Enter the name of the module (module).apk:")
        my_patch_e = ken(apk_name,module)
        print("\n Embedding...........\n")
        my_patch_e.embed_modules()
    elif choice==3:
        print('LSPatch: A non-root Xposed framework extending from LSPosed Rootless implementation of LSPosed framework, integrating Xposed API by inserting dex and so into the target APK.Supported Versions Min: Android 9 Max: In theory, same with LSPosed')
    else:
        print("\n\nunable to hook!")
    print("\n\tDone!")
    print("\n\tScript Made with love")
    print("\n\t©wambugu kinyua ™")
    
            
        
            
            
            
    