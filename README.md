# tatogenerator
a little script to generate some random text


## Reading words from external source

With `--words-other-file` parameter it is now possible to utilize an external words dictionary - for example, from 
[this source](https://github.com/slavkaa/ukraine_dictionary)

Tatogenerator expects the file to be a newline-separated (`\n`) list of files, so you may need to convert these Excel
files to plain text.

### Example:

```shell
$ ./tatogenerator.py --words-other-file ukraine_dictionary/words.txt  --words-count 10
стемніємо поросло літанями tato курінні mama узорові вискочите способності Невідомий

$ head -10 ukraine_dictionary/words.txt
іскристий
іскриста
іскристе
іскристі
іскристого
іскристої
іскристих
іскристому
іскристій
іскристим
```
