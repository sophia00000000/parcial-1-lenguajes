from FiboVisitor import FiboVisitor

class MyFiboVisitor(FiboVisitor):
    def visitProg(self, ctx):
        n = int(ctx.INT().getText())
        return self.fibo(n)

    def fibo(self, n):
        secuencia = [0, 1]
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]
