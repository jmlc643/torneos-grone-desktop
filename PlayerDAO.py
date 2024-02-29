from Conexion import Conexion
from Player import Player


class PlayerDAO:
    SELECT = 'SELECT * FROM player ORDER BY points DESC, percent_difference DESC, percent_for DESC, percent_against DESC, username'
    SELECT_ID = 'SELECT * FROM player WHERE id = %s'
    INSERT = 'INSERT INTO player (username, points, percent_for, percent_against, percent_difference, won, drawn, lost) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    UPDATE = 'UPDATE player SET username = %s, points = %s, percent_for = %s, percent_against = %s, percent_difference = %s, won = %s, drawn = %s, lost = %s WHERE id = %s'
    DELETE = 'DELETE FROM player WHERE id = %s'

    @classmethod
    def select(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECT)
            registros = cursor.fetchall()
            # Mapeo de clase - tabla clientes
            players = []
            for registro in registros:
                player = Player(registro[0], registro[1], registro[3], registro[4], registro[6], registro[7], registro[8])
                players.append(player)
            return players
        except Exception as e:
            print(f'An error occurred while trying to select: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def select_by_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECT_ID, valores)
            registro = cursor.fetchone()
            # Mapeo de la clase-tabla cliente
            player = Player(registro[0], registro[1], registro[3], registro[4], registro[6], registro[7], registro[8])
            return player
        except Exception as e:
            print(f'An error occurred while trying to select by id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insert(cls, player):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (player.username, player.points, player.percent_for, player.percent_against, player.percent_difference, player.won, player.drawn, player.lost)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'An error occurred while trying to insert: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def update(cls, player):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            selected_player = cls.select_by_id(player.id)
            # Solving the problem of lost and problem of name
            if player.lost != 0:
                lost = player.lost
            else: lost = selected_player.lost
            if player.username != '':
                username = player.username
            else: username = selected_player.username
            # Solving the problem of the points
            if player.won != 0:
                won = player.won
            else: won = selected_player.won
            if player.drawn != 0:
                drawn = player.drawn
            else: drawn = selected_player.drawn
            points = selected_player.calculate_points(won, drawn)
            # Solving the problem of the percent difference
            if player.percent_for != 0:
                percent_for = player.percent_for
            else: percent_for = selected_player.percent_for
            if player.percent_against != 0:
                percent_against = player.percent_against
            else: percent_against = selected_player.percent_against
            percent_difference = selected_player.calculate_difference(percent_for, percent_against)
            # Executa UPDATE Command
            valores = (username, points, percent_for, percent_against, percent_difference, won, drawn, lost, player.id)
            cursor.execute(cls.UPDATE, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'An error ocurred while trying to update: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def delete(cls, player):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (player.id,)
            cursor.execute(cls.DELETE, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'An error occurred while trying to delete: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    # INSERT
    """
    player1 = Player(username = 'ABC', won = 10, lost = 2, drawn = 1, percent_for = 20, percent_against = 20)
    inserted_players = PlayerDAO.insert(player1)
    print(f'Inserted players : {inserted_players}')
    """

    # SELECT
    """
    players = PlayerDAO.select()
    for player in players:
        print(player)
    """

    # SELECT BY ID
    """
    player = PlayerDAO.select_by_id(1)
    print(player)
    """

    # DELETE
    """
    player_delete = Player(id=1)
    deleted_players = PlayerDAO.delete(player_delete)
    print(f'Deleted players: {deleted_players}')
    """

    # UPDATE
    """
    player = Player(2, "Mordecai Grone", won = 5, percent_against = 10 )
    updated_player = PlayerDAO.update(player)
    print(f'Updated player: {updated_player}')
    """