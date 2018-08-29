---
layout: page
permalink: how-to-create-console-application
title: Как создать простое консольное приложение
---

### Создание проекта

Запускаем visual studio. Создаем новый проект:

![](/assets/images/how-to-create-console-application/create_console_app_01.png)

В открывшемся окне, выбираем пункт **Консольное приложение (.NET Framework)**

![](/assets/images/how-to-create-console-application/create_console_app_02.png)

вводим имя приложения **FirstApp**, остальное в этот раз можно не трогать, жмем **Ok**.

Откроется код приложение, так как у нас приложение пока самое простое оно состоит из одного файла:

![](/assets/images/how-to-create-console-application/create_console_app_03.png)

### Разбор кода

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
 * вы оборачиваете их в разные пространства имен, и одна функция вывзывается как
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

### Добавляем вывод в консоль

Запустим программу, нажав кнопку пуск

![](/assets/images/how-to-create-console-application/create_console_app_04.png)

запустится сборка приложения (то есть преобразование C# кода в бинарный код для вирутальной машины .NET), откроется окно консоли и тут же закроется.

Открывается и закрывается окно потому, что наше приложение пока еще ничего не делает.

Давайте выведем чего-нибудь в консоль. Для этого воспользуемся классом Console, которые находится в пакете System (именно для этого и нужна строчка **using System**), и так:

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

Снова что-то проскакивает уже с нашим текстом, но все равно быстро закрывается.

Надо как-нибудь остановить процесс мнгновенного закрытия программы. Для этого заставим прогамму ждать нажатия любой клавиши от пользователя, правим приложение:

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


