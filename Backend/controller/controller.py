import xml.etree.ElementTree as ET

def Mensaje(msj = None):
    
    if (msj != None):
        root = ET.fromstring(msj)
        elnombre = ""
        for child in root:
            print(child.text)
            elnombre = child.text
        return (
            '''
            <respuesta>
                <mensaje>Mensaje enviado por: '''+elnombre+'''
            </respuesta>
            '''
           )
    return (
        '''
        <respuesta>
            <mensaje>Hola Messi
        </respuesta>
        '''
    )
