def on_error():
    while True:
        try:
            x = int(input('Un nombre : '))
            break
        except (TypeError, IOError):
            pass
        except ValueError:
            print('Ce n\'est pas un nombre valide. Recommencez...')
        except IndexError as e:
            print('Erreur index', e)
        except:
            print("?")