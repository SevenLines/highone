---
layout: page
permalink: how-to-create-console-application
title: Как создать простое консольное приложение
comments: true
---

## Создание проекта

Запускаем visual studio. Создаем новый проект:

![](/assets/images/how-to-create-console-application/create_console_app_01.png)

В открывшемся окне, выбираем пункт **Консольное приложение (.NET Framework)**

![](/assets/images/how-to-create-console-application/create_console_app_02.png)

вводим имя приложения **FirstApp**, остальное в этот раз можно не трогать, жмем **Ok**.

Откроется код приложения. Так как у нас приложение пока самое простое, оно состоит из одного файла:

![](/assets/images/how-to-create-console-application/create_console_app_03.png)

## Разбор кода

Тут может встретиться куча странных и непонятных слов, в принципе этот раздел можно пропустить.

{% highlight csharp %}
/**
 * все что начинается с using 
 * это набор пакетов (своего рода расширений)
 * для доступа к разным специфическим функциям и классам
 * например для доступа к консоли, файлам и т. д.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/**
 * namespace это так называемое пространство имен,
 * которое используется для минимизации конфликтов имен в названиях классов, функций и т.п.
 * Конфликт имен - это когда например вы создали две функции с одинаковыми названиями,
 * но которые реализуют разную логику. Чтобы знать какую функцию вызывать, 
 * вы оборачиваете их в разные пространства имен, и одна функция вызывается как
 * namespace1.func(), а другая namespace2.func()
 */ 
namespace FirstApp 
{
    /**
     * Program -- класс нашей программы, для любой программа создается базовый класс
     * класс используется для группировки логики приложения
     */
    class Program
    {
        /**
         * Main -- это та функция, с которой начинается исполнение программы
         * static -- значит что функцию можно вызывать не создавая экземпляр класса
         * void -- функцию не возвращает никаких значений
         * string[] args -- это параметры, которые передаются при запуске приложения
         */
        static void Main(string[] args)
        {
        }
    }
}
{% endhighlight %}

## Добавляем вывод в консоль

Запустим программу, нажав кнопку пуск

![](/assets/images/how-to-create-console-application/create_console_app_04.png)

запустится сборка приложения (то есть преобразование C# кода в бинарный код для виртуальной машины .NET). 

Затем откроется окно консоли и тут же закроется. Это, между прочим, была наша программа в действии. 

Открывается и закрывается окно потому, что наше приложение пока еще ничего не умеет.

Давайте выведем чего-нибудь в консоль. Для этого воспользуемся классом **Console**, которые находится в пакете **System** (именно для этого и нужна строчка **using System**), и так:

{% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello world"); // добавили строчку
        }
    }
}
{% endhighlight %}

запускаем приложение, либо кликая на кнопку **Пуск** либо нажав **F5**.

Снова что-то проскакивает, но уже с нашим текстом, но все равно быстро закрывается.

Надо как-нибудь остановить процесс мгновенного закрытия программы. Для этого заставим программу ждать нажатия любой клавиши от пользователя, правим приложение:

 {% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello world");
            Console.ReadKey(); // добавили строчку
        }
    }
}
{% endhighlight %}

Отлично! Теперь программа напечатал текст, и остановилась -- ждет пока пользователь чего-нибудь нажмет.

![](/assets/images/how-to-create-console-application/create_console_app_05.png)

Жмем любую клавишу, и программа тут же закрывается.

Поздравляю, теперь у вас есть первое настоящее приложение на C#.

## Исполняемый файл приложения

Итогом компиляции приложения является __*.exe__ файл, именно этот файл запускается, когда нажимаешь кнопку пуск. 
Точнее, сначала этот файл создается, а потом уже запускается. Сам файл лежит по пути, который был указан при создании проекта.

В моем случае я указал имя приложения **FirstApp**, а путь к проекту `C:\Users\m\source\repos`. Таким образом exe файл находится в папке `c:\Users\m\source\repos\FirstApp\FirstApp\bin\Debug\`

![](/assets/images/how-to-create-console-application/create_console_app_06.png)

Вы можете запустить приложение `FirstApp` и убедится, что он действительно является вашей программой.

Возможно вы обратили внимание что в этой же папке лежат еще два файла:

* FirstApp.pdb -- это файл, который используется Visual Studio для отладки приложения.
* FirstApp.exe.config -- это файл, в который можно сохранять различные настройки приложения.


