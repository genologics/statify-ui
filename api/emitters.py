from piston.emitters import Emitter

class TextEmitter(Emitter):
    def render(self, request):
        return self.data

Emitter.register('text', TextEmitter, 'text/plain; charset=utf-8')