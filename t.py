import gdown
home = os.getenv("U2NET_HOME", os.path.join("~", ".u2net"))
    # home = "models"
   
path = Path(home).expanduser() / f"{model_name}.onnx"

path.parents[0].mkdir(parents=True, exist_ok=True)
    
md5 = "60024c5c889badc19c04ad937298a77b"
url = "https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab"
gdown.download(url, str(path), use_cookies=False)
