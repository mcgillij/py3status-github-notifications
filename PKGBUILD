# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-github-notifications
pkgdesc="Python module for py3status to keep track of your Github notifications."
pkgver=0.1.2
pkgrel=1
arch=('any')
license=('MIT')
makedepends=('python-setuptools' "python-dephell")
url="https://github.com/mcgillij/py3status-github-notifications"
#source=("https://github.com/mcgillij/py3status-github-notifications/releases/download/0.1.2/py3status-github-notifications-0.1.2.tar.gz")
source=("py3status-github-notifications-0.1.2.tar.gz")
md5sums=('ab135b2b9e69e33fa8b06fa6d1622f56')

prepare() {
  cd "$pkgname-$pkgver"
  dephell deps convert --from pyproject.toml --to setup.py
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1 --skip-build
}
