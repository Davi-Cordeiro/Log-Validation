#Código para analisar logs e exibir caso 
#tenha algum usuário dando comando repetido.
#Este código também capta os erros e os ignora
#para não ter interferência no código e afetar
#na execução.

class ProcessingLogs:
    #Resgatando logs de arquivo.txt 
    def __init__(self):
        #Caminho das logs salvas
        self.path = "/home/davi/Documentos/Processamento log/logs.txt"
        
        #Listas e dicionário para facilitar a validação e captação dos comandos
        self.logs = [] 
        self.dict_user = {}
        self.status = []
        self.dict_valid_command = {}

        #Contadores
        self.valid_logs = 0
        self.valid_logout = 0 
        self.user_command_valid = 0

    def parsing_logs(self):
        with open(self.path, "r") as file:

            #Separa entre "Horário: Usuário: Ação" para ficar mais fácil a captação de comandos repetidos
            for lines in file:
                part = lines.split(';')
                
                if len(part) < 3:
                    continue
                    
                parts =  part[0], part[1], part[2] # part[0]:horário----part[1]:usuário----part[2]:ação
                self.logs.append(parts)

    def validation_logs(self):
        for user in self.logs:
            #Código de login do usuário
            if "LOGIN" in user[2]:
                if user[1] in self.dict_user and self.dict_user[user[1]] is True:
                        self.status.append(f"{user[0]}:ERRO: {user[1]} already Logged in")
                        
                else:
                    self.dict_user[user[1]] = True
                    self.status.append(f"{user[0]}:The user {user[1]} is Logged in")
                    self.valid_logs += 1
                    


            #Código de logout do usuário
            elif "LOGOUT" in user[2]:
                if user[1] not in self.dict_user or self.dict_user[user[1]] is False:
                        self.status.append(f"{user[0]}:ERRO: User {user[1]} already Logged Out")
                        self.valid_logout +=1
                
                else:    
                    self.dict_user[user[1]] = False
                    self.status.append(f"{user[0]}:The user {user[1]} is Logged Out")

            #Caso ocorra algum erro inesperado
            elif "ERROR" in user[2]:
                self.status.append(f"{user[0]}:ERRO no usuário {user[1]}")

            
    def report_logs(self):
        self.path = "/home/davi/Documentos/Processamento log/logs_report.txt"

        with open(self.path, 'w') as file:
            for status in self.status:
                file.write(f"{status}\n")
            
            file.write(
                f"""\nREPORT LOGS!
Logs successfully completed: {self.valid_logs}
Logout successfully completed: {self.valid_logout}"""
            )


logs = ProcessingLogs()
logs.parsing_logs()
logs.validation_logs()
logs.report_logs()
