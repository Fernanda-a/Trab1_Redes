class DefaultPage:
    PAGES = dict()

    def __init__(self, brython):
        self.brython = brython
        self.page = self.chat()
        #[item.bind("click", self.link) for item in self.items]

    def show(self):
    # Primeiro ela limpa o HTML
        self.brython.document["changingPart"].html = ""
        # Depois bota a página como filho da div pydiv
        _ = self.brython.document["changingPart"] <= self.page

    def build_body(self):
        return ()
    
    def chat(self):
        h = self.brython.html
        cnt = h.DIV(self.build_body())
        return cnt

        
class OptionsPage(DefaultPage):
    def __init__(self, brython):
        super().__init__(brython)

    def build_body(self):
        h = self.brython.html
        inf = h.DIV("", Class="informationModal container is-flex is-justify-content-center is-align-items-center")
        tex = h.P("1 - Criar usuário <br> 2 - Autenticar usuário <br> 3 - Enviar mensagens <br> 0 - Sair", Class="informationModal",  style={'color':'black', 'textShadow':'0.3rem 0rem 0.2rem whitesmoke'})
        inpdiv = h.DIV("", Class="messageInput is-flex is-justify-content-space-between is-absolute mt-6", style={'position': 'fixed', 'bottom': '7%', 'right': '19%', 'width': '58rem'})
        inp = h.INPUT(type="text", name="messageInput", Class="input is-rounded mr-2", placeholder="Escolha uma opção...")
        inpbut = h.BUTTON("Send", type="button", name="sendButton", Class="button is-rounded")
        inpdiv <= ((inp, inpbut))
        return (inf, tex, inpdiv)
    
class ClientPage(DefaultPage):
    #the client must be created and verified with this page :)
    
class MessagePage(DefaultPage):
    
# MENU_OPTIONS = tuple(zip("PROJETO CONHECIMENTO PESQUISA PERGUNTAS LOGIN USER RASCUNHO ESCREVER ARTIGO".split(),
#                          "bars-progress book book-medical question right-to-bracket user".split()))

# # Aqui uma base de página é criado.
# class SimplePage:
#     # Aqui está declarando os atributos da classe
#     def __init__(self, brython, menu=MENU_OPTIONS, hero="none_hero"):
#         #     item.bind("click", self.link)
#         [item.bind("click", self.link) for item in self.items]

#     # essa função pega o id do algo que foi clicado e mostra a página que contém esse id e está dentro do dic PAGES.
#     def link(self, ev=None):
#         msg = document['messageInput'].value

#         match msg:
#             case "0":
#                 #sair
#                 self.PAGES[page].show()
#             case "1":
#                 #criar usurario
#                 self.PAGES[page].show()
#             case "2":
#                 #verificar user
#                 self.PAGES[page].show()
#             case "3":
#                 #enviar msg
#                 self.PAGES[page].show()
#             case default:
#                 #mandar mensagem de opção invalida
#                 print("ehe")

#     #Essa função definitivamente faz a página aparecer na tela. Ela é utilizada na funcção anterior.
#     def show(self):
#         self.brython.document["changingPart"].html = ""
#         _ = self.brython.document["changingPart"] <= self.page

#     #Não sei o que faz
#     def build_body(self):
#         return ()

#     # Essa função constrói a barra de pesquisa
#     def navigator(self, menu):
#         h = self.brython.html

#         def do_item(title=None, icon=None):
#             spn = h.SPAN(
#                 h.I(Class=f"fa fa-lg fa-{icon}", Id=f"-_{title}_-") + h.SPAN(title, Id=f"_{title}_-"),
#                 Class="icon-text", style="color: #333;", Id=f"-_{title}_--")
#             return h.A(spn, Id=f"_{title}_", Class="navbar-item", href="./#")

#         aim = h.IMG(src="/src/arvora/_media/arvora_ico.png", alt="Arvora", height="28", Id="_MAIN_-")
#         arv = h.A(aim, Id="_MAIN_", Class="navbar-item", href="./")
#         nbr = h.DIV(arv, Class="navbar-brand", Id="-_MAIN_-")
#         self.items = [do_item(**item) for item in menu]
#         end = h.DIV(self.items[-1], Class="navbar-end")
#         self.items = items = [nbr] + self.items[:-1] + [end]
#         nav = h.NAV(items, Class="navbar")
#         fna = h.DIV(h.DIV(nav, Class="container"), Class="first_nav")
#         return fna
    
class Site:
    def __init__(self, br):
        self.brython = br

    def start(self):
        br = self.brython
        # Aqui as o nome das páginas são lincadas com as respectivas classes das páginas
        # SimplePage.PAGES = {f"_{page}_": SimplePage(br) for page, in PAGES()}
        # SimplePage.PAGES["_MAIN_"] = LandingPage(br)
        # SimplePage.PAGES["_PESQUISA_"] = PesquisaPage(br)
        # SimplePage.PAGES["_LOGIN_"] = LoginPage(br)
        # SimplePage.PAGES['_CADASTRO_'] = CadastroPage(br)
        # SimplePage.PAGES["_PROJETO_"] = ProjectPage(br)
        # SimplePage.PAGES["_CONHECIMENTO_"] = KnowledgePage(br)
        # SimplePage.PAGES["_ARTIGO_"] = Article(br)
        # # SimplePage.PAGES['_PERGUNTAS_'] = QuestionsPage(br)
        # SimplePage.PAGES["_RASCUNHO_"] = DraftPage(br)
        # SimplePage.PAGES["_ESCREVER_"] = WritingPage(br)

        _main = OptionsPage(br)
        _main.show()
        return _main


def main(br):
    return Site(br).start()
