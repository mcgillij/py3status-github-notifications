# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-github-notifications
pkgdesc="Python module for py3status to keep track of your Github notifications."
pkgver=0.1.5
pkgrel=1
arch=('any')
license=('MIT')
makedepends=('python-setuptools')
url="https://github.com/mcgillij/py3status-github-notifications"
source=("https://github.com/mcgillij/py3status-github-notifications/releases/download/$pkgver/py3status-github-notifications-$pkgver.tar.gz")
md5sums=('b50c30e4e4c726826c505850503010d3')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1 --skip-build
}
