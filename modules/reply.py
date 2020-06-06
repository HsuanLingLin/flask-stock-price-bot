from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn
)

# 官方文件
# https://github.com/line/line-bot-sdk-python


faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '照片': ImageSendMessage(
        original_content_url='https://picsum.photos/id/1040/900/400',
        preview_image_url='https://picsum.photos/id/1040/900/400'
    ),
    '電話': TextSendMessage(text='0912-345-678'),
    '地址': LocationSendMessage(
        title='my location',
        address='Taiwan',
        # 緯度
        latitude=25.0194203,
        # 經度
        longitude=121.541459
    )
}

# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            # 卡片一
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
                title='推薦群組一',
                text='電子股',
                # 一個action 最多三個按鈕
                actions=[
                    MessageAction(
                        # 按鈕上會顯示的文字
                        label='台積電(2330)',
                        # user點擊後會幫忙寫的文字，有的text很複雜，可以靠這個幫他寫
                        text='2330'
                    ),
                    MessageAction(
                        label='中華電(2412)',
                        text='2412'
                    ),
                    MessageAction(
                        label='鴻海(2317)',
                        text='2317'
                    )
                ]
            ),
            # 卡片二
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://images.unsplash.com/photo-1534951009808-766178b47a4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
                title='推薦群組二',
                text='金融股',
                actions=[
                    MessageAction(
                        label='兆豐金(2886)',
                        text='2886'
                    ),
                    MessageAction(
                        label='玉山金(2884)',
                        text='2884'
                    ),
                    MessageAction(
                        label='中信金(2891)',
                        text='2891'
                    )
                ]
            )
        ]
    )
)
