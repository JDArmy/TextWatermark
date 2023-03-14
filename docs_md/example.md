# Example

## BINARY_REPRESENTATION

--template-chars-key can be set to any key in [combining_chars](/templates/#combining_chars), [invisible_chars](/templates/#invisible_chars) and [whitespace_chars](/templates/#whitespace_chars)

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t BINARY_REPRESENTATION -k '\u0300'

    1̀月10̀日,美图公司̀创̀始人兼C̀EO吴欣鸿发̀送了̀一封内部̀全̀员邮件,涉̀及̀经̀营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "BINARY_REPRESENTATION", "confusables_chars": [], "confusables_chars_key": "̀", "wm_base": 2, "method": "APPEND_AS_BINARY", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'
    
    The retrieved watermark is: 123456
    ```

## COMBINING_CHARS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t COMBINING_CHARS

    1́月́1̀0̑日̆,̀美̌图́公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "COMBINING_CHARS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 36, "method": "APPEND_TO_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 8, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## FONT_COLOR

--template-chars-key can be set to any key in [font_color](/templates/#font_color)

=== "Insert"
    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t FONT_COLOR -k 'black4'

    <span style="color: #444">1</span><span style="color: #000">月</span><span style="color: #000">1</span><span style="color: #444">0</span><span style="color: #000">日</span><span style="color: #000">,</span><span style="color: #000">美</span><span style="color: #000">图</span><span style="color: #000">公</span><span style="color: #444">司</span><span style="color: #444">创</span><span style="color: #000">始</span><span style="color: #000">人</span><span style="color: #000">兼</span><span style="color: #444">C</span><span style="color: #000">E</span><span style="color: #000">O</span><span style="color: #000">吴</span><span style="color: #000">欣</span><span style="color: #000">鸿</span><span style="color: #444">发</span><span style="color: #000">送</span><span style="color: #444">了</span><span style="color: #000">一</span><span style="color: #000">封</span><span style="color: #000">内</span><span style="color: #444">部</span><span style="color: #444">全</span><span style="color: #000">员</span><span style="color: #000">邮</span><span style="color: #000">件</span><span style="color: #000">,</span><span style="color: #444">涉</span><span style="color: #444">及</span><span style="color: #444">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    <span style="color: #444">1</span><span style="color: #000">月</span><span style="color: #000">1</span><span style="color: #444">0</span><span style="color: #000">日</span><span style="color: #000">,</span><span style="color: #000">美</span><span style="color: #000">图</span><span style="color: #000">公</span><span style="color: #444">司</span><span style="color: #444">创</span><span style="color: #000">始</span><span style="color: #000">人</span><span style="color: #000">兼</span><span style="color: #444">C</span><span style="color: #000">E</span><span style="color: #000">O</span><span style="color: #000">吴</span><span style="color: #000">欣</span><span style="color: #000">鸿</span><span style="color: #444">发</span><span style="color: #000">送</span><span style="color: #444">了</span><span style="color: #000">一</span><span style="color: #000">封</span><span style="color: #000">内</span><span style="color: #444">部</span><span style="color: #444">全</span><span style="color: #000">员</span><span style="color: #000">邮</span><span style="color: #000">件</span><span style="color: #000">,</span><span style="color: #444">涉</span><span style="color: #444">及</span><span style="color: #444">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "FONT_COLOR", "confusables_chars": [], "confusables_chars_key": "black4", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## FONT_FLOAT

--template-chars-key can be set to any key in [font_float](/templates/#font_float)

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t FONT_FLOAT -k 'up3'  

    <span style="display: inline-block;position: relative;top:-3px;">1</span><span style="display: inline-block;position: relative;top:0;">月</span><span style="display: inline-block;position: relative;top:0;">1</span><span style="display: inline-block;position: relative;top:-3px;">0</span><span style="display: inline-block;position: relative;top:0;">日</span><span style="display: inline-block;position: relative;top:0;">,</span><span style="display: inline-block;position: relative;top:0;">美</span><span style="display: inline-block;position: relative;top:0;">图</span><span style="display: inline-block;position: relative;top:0;">公</span><span style="display: inline-block;position: relative;top:-3px;">司</span><span style="display: inline-block;position: relative;top:-3px;">创</span><span style="display: inline-block;position: relative;top:0;">始</span><span style="display: inline-block;position: relative;top:0;">人</span><span style="display: inline-block;position: relative;top:0;">兼</span><span style="display: inline-block;position: relative;top:-3px;">C</span><span style="display: inline-block;position: relative;top:0;">E</span><span style="display: inline-block;position: relative;top:0;">O</span><span style="display: inline-block;position: relative;top:0;">吴</span><span style="display: inline-block;position: relative;top:0;">欣</span><span style="display: inline-block;position: relative;top:0;">鸿</span><span style="display: inline-block;position: relative;top:-3px;">发</span><span style="display: inline-block;position: relative;top:0;">送</span><span style="display: inline-block;position: relative;top:-3px;">了</span><span style="display: inline-block;position: relative;top:0;">一</span><span style="display: inline-block;position: relative;top:0;">封</span><span style="display: inline-block;position: relative;top:0;">内</span><span style="display: inline-block;position: relative;top:-3px;">部</span><span style="display: inline-block;position: relative;top:-3px;">全</span><span style="display: inline-block;position: relative;top:0;">员</span><span style="display: inline-block;position: relative;top:0;">邮</span><span style="display: inline-block;position: relative;top:0;">件</span><span style="display: inline-block;position: relative;top:0;">,</span><span style="display: inline-block;position: relative;top:-3px;">涉</span><span style="display: inline-block;position: relative;top:-3px;">及</span><span style="display: inline-block;position: relative;top:-3px;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    <span style="display: inline-block;position: relative;top:-3px;">1</span><span style="display: inline-block;position: relative;top:0;">月</span><span style="display: inline-block;position: relative;top:0;">1</span><span style="display: inline-block;position: relative;top:-3px;">0</span><span style="display: inline-block;position: relative;top:0;">日</span><span style="display: inline-block;position: relative;top:0;">,</span><span style="display: inline-block;position: relative;top:0;">美</span><span style="display: inline-block;position: relative;top:0;">图</span><span style="display: inline-block;position: relative;top:0;">公</span><span style="display: inline-block;position: relative;top:-3px;">司</span><span style="display: inline-block;position: relative;top:-3px;">创</span><span style="display: inline-block;position: relative;top:0;">始</span><span style="display: inline-block;position: relative;top:0;">人</span><span style="display: inline-block;position: relative;top:0;">兼</span><span style="display: inline-block;position: relative;top:-3px;">C</span><span style="display: inline-block;position: relative;top:0;">E</span><span style="display: inline-block;position: relative;top:0;">O</span><span style="display: inline-block;position: relative;top:0;">吴</span><span style="display: inline-block;position: relative;top:0;">欣</span><span style="display: inline-block;position: relative;top:0;">鸿</span><span style="display: inline-block;position: relative;top:-3px;">发</span><span style="display: inline-block;position: relative;top:0;">送</span><span style="display: inline-block;position: relative;top:-3px;">了</span><span style="display: inline-block;position: relative;top:0;">一</span><span style="display: inline-block;position: relative;top:0;">封</span><span style="display: inline-block;position: relative;top:0;">内</span><span style="display: inline-block;position: relative;top:-3px;">部</span><span style="display: inline-block;position: relative;top:-3px;">全</span><span style="display: inline-block;position: relative;top:0;">员</span><span style="display: inline-block;position: relative;top:0;">邮</span><span style="display: inline-block;position: relative;top:0;">件</span><span style="display: inline-block;position: relative;top:0;">,</span><span style="display: inline-block;position: relative;top:-3px;">涉</span><span style="display: inline-block;position: relative;top:-3px;">及</span><span style="display: inline-block;position: relative;top:-3px;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "FONT_FLOAT", "confusables_chars": [], "confusables_chars_key": "up3", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## FONT_SIZE

--template-chars-key can be set to any key in [font_size](/templates/#font_size)

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t FONT_SIZE -k '110' 

    <span style="font-size: 110%">1</span><span style="font-size: 100%">月</span><span style="font-size: 100%">1</span><span style="font-size: 110%">0</span><span style="font-size: 100%">日</span><span style="font-size: 100%">,</span><span style="font-size: 100%">美</span><span style="font-size: 100%">图</span><span style="font-size: 100%">公</span><span style="font-size: 110%">司</span><span style="font-size: 110%">创</span><span style="font-size: 100%">始</span><span style="font-size: 100%">人</span><span style="font-size: 100%">兼</span><span style="font-size: 110%">C</span><span style="font-size: 100%">E</span><span style="font-size: 100%">O</span><span style="font-size: 100%">吴</span><span style="font-size: 100%">欣</span><span style="font-size: 100%">鸿</span><span style="font-size: 110%">发</span><span style="font-size: 100%">送</span><span style="font-size: 110%">了</span><span style="font-size: 100%">一</span><span style="font-size: 100%">封</span><span style="font-size: 100%">内</span><span style="font-size: 110%">部</span><span style="font-size: 110%">全</span><span style="font-size: 100%">员</span><span style="font-size: 100%">邮</span><span style="font-size: 100%">件</span><span style="font-size: 100%">,</span><span style="font-size: 110%">涉</span><span style="font-size: 110%">及</span><span style="font-size: 110%">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    <span style="font-size: 110%">1</span><span style="font-size: 100%">月</span><span style="font-size: 100%">1</span><span style="font-size: 110%">0</span><span style="font-size: 100%">日</span><span style="font-size: 100%">,</span><span style="font-size: 100%">美</span><span style="font-size: 100%">图</span><span style="font-size: 100%">公</span><span style="font-size: 110%">司</span><span style="font-size: 110%">创</span><span style="font-size: 100%">始</span><span style="font-size: 100%">人</span><span style="font-size: 100%">兼</span><span style="font-size: 110%">C</span><span style="font-size: 100%">E</span><span style="font-size: 100%">O</span><span style="font-size: 100%">吴</span><span style="font-size: 100%">欣</span><span style="font-size: 100%">鸿</span><span style="font-size: 110%">发</span><span style="font-size: 100%">送</span><span style="font-size: 110%">了</span><span style="font-size: 100%">一</span><span style="font-size: 100%">封</span><span style="font-size: 100%">内</span><span style="font-size: 110%">部</span><span style="font-size: 110%">全</span><span style="font-size: 100%">员</span><span style="font-size: 100%">邮</span><span style="font-size: 100%">件</span><span style="font-size: 100%">,</span><span style="font-size: 110%">涉</span><span style="font-size: 110%">及</span><span style="font-size: 110%">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "FONT_SIZE", "confusables_chars": [], "confusables_chars_key": "110", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## FONT_STYLE

--template-chars-key can be set to any key in [font_style](/templates/#font_style)

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t FONT_STYLE -k 'text-decoration-underline'

    <span style="text-decoration:underline;">1</span><span style="text-decoration:none;">月</span><span style="text-decoration:none;">1</span><span style="text-decoration:underline;">0</span><span style="text-decoration:none;">日</span><span style="text-decoration:none;">,</span><span style="text-decoration:none;">美</span><span style="text-decoration:none;">图</span><span style="text-decoration:none;">公</span><span style="text-decoration:underline;">司</span><span style="text-decoration:underline;">创</span><span style="text-decoration:none;">始</span><span style="text-decoration:none;">人</span><span style="text-decoration:none;">兼</span><span style="text-decoration:underline;">C</span><span style="text-decoration:none;">E</span><span style="text-decoration:none;">O</span><span style="text-decoration:none;">吴</span><span style="text-decoration:none;">欣</span><span style="text-decoration:none;">鸿</span><span style="text-decoration:underline;">发</span><span style="text-decoration:none;">送</span><span style="text-decoration:underline;">了</span><span style="text-decoration:none;">一</span><span style="text-decoration:none;">封</span><span style="text-decoration:none;">内</span><span style="text-decoration:underline;">部</span><span style="text-decoration:underline;">全</span><span style="text-decoration:none;">员</span><span style="text-decoration:none;">邮</span><span style="text-decoration:none;">件</span><span style="text-decoration:none;">,</span><span style="text-decoration:underline;">涉</span><span style="text-decoration:underline;">及</span><span style="text-decoration:underline;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    <span style="text-decoration:underline;">1</span><span style="text-decoration:none;">月</span><span style="text-decoration:none;">1</span><span style="text-decoration:underline;">0</span><span style="text-decoration:none;">日</span><span style="text-decoration:none;">,</span><span style="text-decoration:none;">美</span><span style="text-decoration:none;">图</span><span style="text-decoration:none;">公</span><span style="text-decoration:underline;">司</span><span style="text-decoration:underline;">创</span><span style="text-decoration:none;">始</span><span style="text-decoration:none;">人</span><span style="text-decoration:none;">兼</span><span style="text-decoration:underline;">C</span><span style="text-decoration:none;">E</span><span style="text-decoration:none;">O</span><span style="text-decoration:none;">吴</span><span style="text-decoration:none;">欣</span><span style="text-decoration:none;">鸿</span><span style="text-decoration:underline;">发</span><span style="text-decoration:none;">送</span><span style="text-decoration:underline;">了</span><span style="text-decoration:none;">一</span><span style="text-decoration:none;">封</span><span style="text-decoration:none;">内</span><span style="text-decoration:underline;">部</span><span style="text-decoration:underline;">全</span><span style="text-decoration:none;">员</span><span style="text-decoration:none;">邮</span><span style="text-decoration:none;">件</span><span style="text-decoration:none;">,</span><span style="text-decoration:underline;">涉</span><span style="text-decoration:underline;">及</span><span style="text-decoration:underline;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "FONT_STYLE", "confusables_chars": [], "confusables_chars_key": "text-decoration-underline", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## FONT_WEIGHT

--template-chars-key can be set to any key in [font_weight](/templates/#font_weight)

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t FONT_WEIGHT -k 'bolder'

    <span style="font-weight: bolder;">1</span><span style="font-weight: normal;">月</span><span style="font-weight: normal;">1</span><span style="font-weight: bolder;">0</span><span style="font-weight: normal;">日</span><span style="font-weight: normal;">,</span><span style="font-weight: normal;">美</span><span style="font-weight: normal;">图</span><span style="font-weight: normal;">公</span><span style="font-weight: bolder;">司</span><span style="font-weight: bolder;">创</span><span style="font-weight: normal;">始</span><span style="font-weight: normal;">人</span><span style="font-weight: normal;">兼</span><span style="font-weight: bolder;">C</span><span style="font-weight: normal;">E</span><span style="font-weight: normal;">O</span><span style="font-weight: normal;">吴</span><span style="font-weight: normal;">欣</span><span style="font-weight: normal;">鸿</span><span style="font-weight: bolder;">发</span><span style="font-weight: normal;">送</span><span style="font-weight: bolder;">了</span><span style="font-weight: normal;">一</span><span style="font-weight: normal;">封</span><span style="font-weight: normal;">内</span><span style="font-weight: bolder;">部</span><span style="font-weight: bolder;">全</span><span style="font-weight: normal;">员</span><span style="font-weight: normal;">邮</span><span style="font-weight: normal;">件</span><span style="font-weight: normal;">,</span><span style="font-weight: bolder;">涉</span><span style="font-weight: bolder;">及</span><span style="font-weight: bolder;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    <span style="font-weight: bolder;">1</span><span style="font-weight: normal;">月</span><span style="font-weight: normal;">1</span><span style="font-weight: bolder;">0</span><span style="font-weight: normal;">日</span><span style="font-weight: normal;">,</span><span style="font-weight: normal;">美</span><span style="font-weight: normal;">图</span><span style="font-weight: normal;">公</span><span style="font-weight: bolder;">司</span><span style="font-weight: bolder;">创</span><span style="font-weight: normal;">始</span><span style="font-weight: normal;">人</span><span style="font-weight: normal;">兼</span><span style="font-weight: bolder;">C</span><span style="font-weight: normal;">E</span><span style="font-weight: normal;">O</span><span style="font-weight: normal;">吴</span><span style="font-weight: normal;">欣</span><span style="font-weight: normal;">鸿</span><span style="font-weight: bolder;">发</span><span style="font-weight: normal;">送</span><span style="font-weight: bolder;">了</span><span style="font-weight: normal;">一</span><span style="font-weight: normal;">封</span><span style="font-weight: normal;">内</span><span style="font-weight: bolder;">部</span><span style="font-weight: bolder;">全</span><span style="font-weight: normal;">员</span><span style="font-weight: normal;">邮</span><span style="font-weight: normal;">件</span><span style="font-weight: normal;">,</span><span style="font-weight: bolder;">涉</span><span style="font-weight: bolder;">及</span><span style="font-weight: bolder;">经</span>营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "FONT_WEIGHT", "confusables_chars": [], "confusables_chars_key": "bolder", "wm_base": 2, "method": "DECORATE_EACH_CHAR", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## HOMOGRAPH_CHINESE

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t HOMOGRAPH_CHINESE                

    1⽉10日,美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略˴科技创新˴未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    邮件显⽰,美图公司将对全体员工进行股票奖励,这是美图公司与员工共享经营成果˴共赴长期发展的心愿。
    此外,邮件还透露美图位于厦⻔的总部新⼤厦即将启用。据吴欣鸿介绍,新大厦除了全面提升的办公空间,还包括企业展厅、培训中心、直播中心、艺术中心、餐厅、咖啡厅、健身房、图书馆、空中花园等配套设施。
    公开信息显示,美图公司于2020年购买了一栋位于厦门美峰创谷的办公楼,总建筑面积约3.42万平方米。
    那么除了外界最关注的全员股权发放以及入住全新总部大楼外,邮件还透露了哪些重要信息呢？其实余下的信息更值得投资人关注。
    邮件信息,2022年是美图忙中有序、稳中求进的一年。公司对美图秀秀、美颜相机、Wink、美图证件照等几款产品的突破和表现,对AI绘画功能撬动美图海外产品排名攀升表示满意。,此外,伴随着越来越好的市场反馈和财务状况,美图公司全员都收获了久违的信心和斗志。很显然,美图公司无论是高层还是员工,对美图的未来都充满了信心。
    这种内部凝聚的气氛来源于哪呢？据悉,美图公司2022年上半年财报,上半年总收入人民币9.712亿元,同比增长20.5%。截止到2022年6月,美图公司月活跃用户数达2.409亿,环比2021年12月增长4.5%。优秀的业绩下,美图确实有理由对未来保持充分的乐观。
    而2023年是美图成立15周年,美图把这一年看作美图公司的新起点,希望能为用户和客户持续提供更好的影像产品和数字化解决方案,也帮助每一位同事追求和实现更美好的生活目标。
    从实际业务层面看,美图的业务战略已经非常清晰,横向看,C端的VIP订阅业务及B端的SaaS及相关业务都获得了大幅度的逆势成长,月活数据也环比净增；而纵向看,美图也在不断聚焦影像核心能力,通过人工智能,继续深化BC两端业务的竞争壁垒。通过成熟且已被市场检验的商业路径持续发力,投资人有理由看好美图在2023年的业绩表现。
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "HOMOGRAPH_CHINESE", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 2, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 35, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## HOMOGRAPH_LETTERS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t HOMOGRAPH_LETTERS      

    1月10日,美图公司创始人兼ⅭEⵔ吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    邮件显示,美图公司将对全体员工进行股票奖励,这是美图公司与员工共享经营成果、共赴长期发展的心愿。
    此外,邮件还透露美图位于厦门的总部新大厦即将启用。据吴欣鸿介绍,新大厦除了全面提升的办公空间,还包括企业展厅、培训中心、直播中心、艺术中心、餐厅、咖啡厅、健身房、图书馆、空中花园等配套设施。
    公开信息显示,美图公司于2020年购买了一栋位于厦门美峰创谷的办公楼,总建筑面积约3.42万平方米。
    那么除了外界最关注的全员股权发放以及入住全新总部大楼外,邮件还透露了哪些重要信息呢?其实余下的信息更值得投资人关注。
    邮件信息,2022年是美图忙中有序、稳中求进的一年。公司对美图秀秀、美颜相机、W𝐢n𝙠、美图证件照等几款产品的突破和表现,对A𝐈绘画功能撬动美图海外产品排名攀升表示满意。,此外,伴随着越来越好的市场反馈和财务状况,美图公司全员都收获了久违的信心和斗志。很显然,美图公司无论是高层还是员工,对美图的未来都充满了信心。
    这种内部凝聚的气氛来源于哪呢?据悉,美图公司2022年上半年财报,上半年总收入人民币9.712亿元,同比增长20.5%。截止到2022年6月,美图公司月活跃用户数达2.409亿,环比2021年12月增长4.5%。优秀的业绩下,美图确实有理由对未来保持充分的乐观。
    而2023年是美图成立15周年,美图把这一年看作美图公司的新起点,希望能为用户和客户持续提供更好的影像产品和数字化解决方案,也帮助每一位同事追求和实现更美好的生活目标。
    从实际业务层面看,美图的业务战略已经非常清晰,横向看,C端的𝐕I𝖯订阅业务及B端的SaaS及相关业务都获得了大幅度的逆势成长,月活数据也环比净增;而纵向看,美图也在不断聚焦影像核心能力,通过人工智能,继续深化BC两端业务的竞争壁垒。通过成熟且已被市场检验的商业路径持续发力,投资人有理由看好美图在2023年的业绩表现。
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "HOMOGRAPH_LETTERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 8, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 13, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## HOMOGRAPH_NUMBERS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t HOMOGRAPH_NUMBERS   

    Ӏ月Ӏ0日,美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    邮件显示,美图公司将对全体员工进行股票奖励,这是美图公司与员工共享经营成果、共赴长期发展的心愿。
    此外,邮件还透露美图位于厦门的总部新大厦即将启用。据吴欣鸿介绍,新大厦除了全面提升的办公空间,还包括企业展厅、培训中心、直播中心、艺术中心、餐厅、咖啡厅、健身房、图书馆、空中花园等配套设施。
    公开信息显示,美图公司于𝟮𝟎𝟐0年购买了一栋位于厦门美峰创谷的办公楼,总建筑面积约Ⳍ.𝟒𝟚万平方米。
    那么除了外界最关注的全员股权发放以及入住全新总部大楼外,邮件还透露了哪些重要信息呢?其实余下的信息更值得投资人关注。
    邮件信息,𝟤𝟬𝟸2年是美图忙中有序、稳中求进的一年。公司对美图秀秀、美颜相机、Wink、美图证件照等几款产品的突破和表现,对AI绘画功能撬动美图海外产品排名攀升表示满意。,此外,伴随着越来越好的市场反馈和财务状况,美图公司全员都收获了久违的信心和斗志。很显然,美图公司无论是高层还是员工,对美图的未来都充满了信心。
    这种内部凝聚的气氛来源于哪呢?据悉,美图公司2022年上半年财报,上半年总收入人民币9.712亿元,同比增长20.5%。截止到2022年6月,美图公司月活跃用户数达2.409亿,环比2021年12月增长4.5%。优秀的业绩下,美图确实有理由对未来保持充分的乐观。
    而2023年是美图成立15周年,美图把这一年看作美图公司的新起点,希望能为用户和客户持续提供更好的影像产品和数字化解决方案,也帮助每一位同事追求和实现更美好的生活目标。
    从实际业务层面看,美图的业务战略已经非常清晰,横向看,C端的VIP订阅业务及B端的SaaS及相关业务都获得了大幅度的逆势成长,月活数据也环比净增;而纵向看,美图也在不断聚焦影像核心能力,通过人工智能,继续深化BC两端业务的竞争壁垒。通过成熟且已被市场检验的商业路径持续发力,投资人有理由看好美图在2023年的业绩表现。
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 13, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

=== "With --no-flag-bit option"

    ```console
    $ textwatermark -v insert -f /tmp/tmp_for_test_textwatermark.txt -m REAL_NUMBER -t HOMOGRAPH_NUMBERS -x "1977326742" -w "1977326741"  -n

    𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶𝟭

    $ textwatermark retrieve -f /tmp/out.txt -p '{"tpl_type": "HOMOGRAPH_NUMBERS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 7, "method": "FIND_AND_REPLACE", "wm_mode": "REAL_NUMBER", "wm_len": 11, "wm_flag_bit": false, "wm_loop": false, "wm_max": "1977326742", "start_at": 0, "version": "0.3.0"}'

    1977326741
    ```

## HOMOGRAPH_PUNCTUATIONS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -t HOMOGRAPH_PUNCTUATIONS      

    1月10日٫美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    邮件显示٫美图公司将对全体员工进行股票奖励‚这是美图公司与员工共享经营成果、共赴长期发展的心愿。
    此外‚邮件还透露美图位于厦门的总部新大厦即将启用。据吴欣鸿介绍,新大厦除了全面提升的办公空间,还包括企业展厅、培训中心、直播中心、艺术中心、餐厅、咖啡厅、健身房、图书馆、空中花园等配套设施。
    公开信息显示,美图公司于2020年购买了一栋位于厦门美峰创谷的办公楼‚总建筑面积约3.42万平方米。
    那么除了外界最关注的全员股权发放以及入住全新总部大楼外٫邮件还透露了哪些重要信息呢ॽ其实余下的信息更值得投资人关注。
    邮件信息,2022年是美图忙中有序、稳中求进的一年。公司对美图秀秀、美颜相机、Wink、美图证件照等几款产品的突破和表现‚对AI绘画功能撬动美图海外产品排名攀升表示满意。‚此外,伴随着越来越好的市场反馈和财务状况‚美图公司全员都收获了久违的信心和斗志。很显然٫美图公司无论是高层还是员工,对美图的未来都充满了信心。
    这种内部凝聚的气氛来源于哪呢ॽ据悉,美图公司2022年上半年财报,上半年总收入人民币9.712亿元,同比增长20.5%。截止到2022年6月,美图公司月活跃用户数达2.409亿,环比2021年12月增长4.5%。优秀的业绩下,美图确实有理由对未来保持充分的乐观。
    而2023年是美图成立15周年,美图把这一年看作美图公司的新起点,希望能为用户和客户持续提供更好的影像产品和数字化解决方案,也帮助每一位同事追求和实现更美好的生活目标。
    从实际业务层面看,美图的业务战略已经非常清晰,横向看,C端的VIP订阅业务及B端的SaaS及相关业务都获得了大幅度的逆势成长,月活数据也环比净增;而纵向看,美图也在不断聚焦影像核心能力,通过人工智能,继续深化BC两端业务的竞争壁垒。通过成熟且已被市场检验的商业路径持续发力,投资人有理由看好美图在2023年的业绩表现。
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "HOMOGRAPH_PUNCTUATIONS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 3, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 23, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 0, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## HTML_EMPTY_TAGS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -i 1 -t HTML_EMPTY_TAGS                     
    1<abbr></abbr><abbr></abbr><strong></strong><dfn></dfn><bdo></bdo><a></a><var></var><sup></sup><bdo></bdo>月10日, 美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件, 涉及经营战略、 科技创新、 未来发展等多个层面, 同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Web View"

    1<abbr></abbr><abbr></abbr><strong></strong><dfn></dfn><bdo></bdo><a></a><var></var><sup></sup><bdo></bdo>月10日, 美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件, 涉及经营战略、 科技创新、 未来发展等多个层面, 同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "HTML_EMPTY_TAGS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 20, "method": "INSERT_INTO_POSITION", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 9, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 1, "version": "0.3.0"}'

    The retrieved watermark is: 123456
    ```

## INVISIBLE_CHARS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999999 -w 123456 -i 1 -t INVISIBLE_CHARS

    1؜᠌︇᠎︍︌‏︋月10日,美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件,涉及经营战略、科技创新、未来发展等多个层面,同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "INVISIBLE_CHARS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 29, "method": "INSERT_INTO_POSITION", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 8, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999999", "start_at": 1, "version": "0.3.0"}'

    The retrieved watermark is: 123456

    ```

## SPACE_CHARS

=== "Insert"
    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 9 -w 1 -i 1 -t SPACE_CHARS

    1月10日, 美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件, 涉及经营战略、 科技创新、 未来发展等多个层面, 同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "SPACE_CHARS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 6, "method": "FIND_AND_REPLACE", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 3, "wm_flag_bit": true, "wm_loop": false, "wm_max": "9", "start_at": 1, "version": "0.3.0"}'

    The retrieved watermark is: 7
    ```

## WHITESPACE_CHARS

=== "Insert"

    ```console
    $ textwatermark -v insert -f './tests/text/1.txt' -m ALPHA_NUMERICAL -x 999 -w 743 -i 1 -t WHITESPACE_CHARS      
              
    1      月10日, 美图公司创始人兼CEO吴欣鸿发送了一封内部全员邮件, 涉及经营战略、 科技创新、 未来发展等多个层面, 同时吴欣鸿还在这封邮件中透露了美图全员股票激励和搬迁新总部大厦两个消息。
    ……
    ```

=== "Retrieve"

    ```console
    $ textwatermark -v retrieve -f /tmp/out.txt -p '{"tpl_type": "WHITESPACE_CHARS", "confusables_chars": [], "confusables_chars_key": "", "wm_base": 14, "method": "INSERT_INTO_POSITION", "wm_mode": "ALPHA_NUMERICAL", "wm_len": 6, "wm_flag_bit": true, "wm_loop": false, "wm_max": "999", "start_at": 1, "version": "0.3.0"}'

    The retrieved watermark is: 743
    ```
