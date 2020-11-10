from PyQt5 import QtWidgets, QtSql

class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQlite')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión, \n',
                                           'Haz click para Cancelar', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
        return True