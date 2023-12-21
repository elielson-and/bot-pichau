class MainEnv:
    def __init__(self):
        self.config_dir = "./CONFIG.env"

    def login_url(self):  
        with open(self.config_dir, "r") as f:
            data = f.readlines()
            for line in data:
                if "PICHAU_LOGIN" in line:
                    value = line.split("=")[1].strip().lower()
                    return str(value)
                
    def credentials(self):
        email = None
        password = None
        with open(self.config_dir, "r") as f:
            data = f.readlines()
        for line in data:
            if "EMAIL" in line:
                email = line.split("=")[1].strip().lower()
            elif "SENHA" in line:
                password = line.split("=")[1].strip().lower()
        return {"email": email, "password": password}