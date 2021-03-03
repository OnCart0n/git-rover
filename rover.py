from web import create_app
from lib.core.appdata import config

def main():
    # 后续完善配置再改
    app = create_app()
    app.run(debug=config.app.debug)


if __name__ == '__main__':
    main()
