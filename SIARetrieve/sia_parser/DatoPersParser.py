from SIARetrieve.sia_parser.Parser import Parser

class DatoPersParser(Parser):

    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)
        self.data = []
        self.titulos = []
        
        datos = self.html.find_all(class_="cuerpo")
        title = self.html.find_all(class_="titulo-2")
        for i in datos:
            self.data.append(i.text)

        for i in title:
            self.titulos.append(i.text)

        print("0 " + self.data[0])
        
        for i in range(len(self.titulos)):
            print(str(i+1) + " " + self.titulos[i] + " - " + self.data[i+1])

    def get_dni(self):
        return self.data[0].split('\\')[0]

    def get_sexo(self):
        return self.data[1].split('\\')[0]

    def get_edad(self):
        return self.data[2].split(' ')[0]
    
    def get_estado_civil(self):
        return self.data[3].split('\\')[0]

    def get_pais(self):
        return self.data[4].split('\\')[0]

    def get_proc_dir(self):
        return self.data[5].split('\\')[0]

    def get_tipo_dom(self):
        return self.data[6].split('\\')[0]

    def get_proc_muni(self):
        return self.data[7].split('\\')[0]

    def get_proc_depa(self):
        return self.data[8].split('\\')[0]

    def get_proc_pais(self):
        return self.data[9].split('\\')[0]

    def get_proc_tel1(self):
        return self.data[10].split('\\')[0]

    def get_proc_tel2(self):
        return self.data[11].split('\\')[0]

    def get_resi_dir(self):
        return self.data[12].split('\\')[0]

    def get_resi_muni(self):
        return self.data[13].split('\\')[0]

    def get_resi_depa(self):
        return self.data[14].split('\\')[0]

    def get_resi_pais(self):
        return self.data[15].split('\\')[0]

    def get_resi_tel1(self):
        return self.data[16].split('\\')[0]

    def get_resi_tel2(self):
        return self.data[17].split('\\')[0]

    def get_naci_fecha(self):
        return self.data[18].split('\\')[0]

    def get_naci_muni(self):
        return self.data[19].split('\\')[0]

    def get_naci_depa(self):
        return self.data[20].split('\\')[0]

    def get_naci_pais(self):
        return self.data[21].split('\\')[0]

    def get_nacionalidad(self):
        return self.data[22].split('\\')[0]

    def get_mili_numero(self):
        return self.data[23].split('\\')[0]

    def get_mili_clase(self):
        return self.data[24].split('\\')[0]

    def get_mili_distri(self):
        return self.data[25].split('\\')[0]

    def get_mili_situacion(self):
        return self.data[26].split('\\')[0]

    def get_usuario(self):
        return self.data[27].split('\\')[0]

    def get_correo_unal(self):
        return self.data[28].split('\\')[0]

    def get_correo_alterno(self):
        return self.data[29].split('\\')[0]

    def get_grupo_sanguineo(self):
        return self.data[30].split('\\')[0]

    def get_rh(self):
        return self.data[31].split('\\')[0]

    def get_eps(self):
        return self.data[32].split('\\')[0]

    #TODO: Hacer para N historias academicas