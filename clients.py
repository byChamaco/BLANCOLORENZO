import var

class Clientes():

    def validarDni(dni):

        '''código que controla si el dni o nif es correcto'''

        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "0123456789"
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False

        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():

        '''muestra mensaje de dni válido'''

        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print('Has elegido femenino')
            if var.ui.rbtMasc.isChecked():
                print('Has elegido masculino')
        except Exception as error:
            print('Error: %s ' % str(error))

    def selPago():
        try:
            if var.ui.chkEfec.isChecked():
                print('Pagas con efectivo')
            if var.ui.chkTarj.isChecked():
                print('Pagas con tarjeta')
            if var.ui.chkTrans.isChecked():
                print('Pagas con transferencia')
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(self):
        print('Hola')