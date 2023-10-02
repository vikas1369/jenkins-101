import fire

def hello(name="World"):
  return "Hello Vikas %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
