# hok8bu7/fake_g2pPoj.py

class G2p:
    def __init__(self):
        pass

    def __call__(self, texts):
        if isinstance(texts, list):
            return texts
        return [texts]
