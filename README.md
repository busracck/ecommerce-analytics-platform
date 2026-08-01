# E-Commerce Analytics Platform

E-Commerce Analytics Platform, e-ticaret verilerini PostgreSQL üzerinde analiz eden ve sonuçları Streamlit tabanlı interaktif bir dashboard üzerinden sunan yapay zekâ destekli bir veri analizi uygulamasıdır.

Proje; satış, sipariş, müşteri, ödeme, ürün kategorisi ve değerlendirme verilerini görselleştirmenin yanında, kullanıcıların doğal dilde soru sorarak veritabanı üzerinde analiz yapabilmesini sağlar.

Kullanıcının yazdığı soru Google Gemini tarafından PostgreSQL sorgusuna dönüştürülür. Üretilen SQL sorgusu güvenlik kontrolünden geçirilir, PostgreSQL üzerinde çalıştırılır ve sonuç Pandas DataFrame olarak alınır. Sistem daha sonra uygun grafik türünü otomatik olarak seçer ve sorgu sonucunu Gemini ile Türkçe olarak yorumlar.

## Projenin Amacı

Bu projenin amacı, klasik bir e-ticaret dashboard’unu doğal dilde sorgulanabilen bir AI veri analistiyle birleştirmektir.

Uygulama sayesinde kullanıcılar SQL bilmeden aşağıdaki gibi sorular sorabilir:

- En çok sipariş veren 5 şehir hangileridir?
- Aylara göre toplam satış trendi nasıldır?
- En yüksek ciroyu sağlayan ürün kategorileri hangileridir?
- Ortalama değerlendirme puanı en düşük kategoriler hangileridir?
- En çok kullanılan ödeme yöntemi hangisidir?

Sistem bu sorular için gerekli SQL sorgusunu otomatik oluşturur, veritabanında çalıştırır ve sonuçları tablo, grafik ve doğal dil açıklaması şeklinde kullanıcıya sunar.

## Temel Özellikler

- PostgreSQL tabanlı e-ticaret veri modeli
- Streamlit ile interaktif ve modern dashboard
- Toplam müşteri, sipariş, satış ve değerlendirme KPI kartları
- Aylık satış trendi analizi
- En çok satılan ürün kategorileri
- Ödeme yöntemi dağılımı
- Müşteri değerlendirme puanı dağılımı
- Eyaletlere göre sipariş analizi
- Google Gemini ile doğal dilden SQL üretimi
- LLM tarafından üretilen SQL sorguları için güvenlik kontrolü
- SQL sonuçlarının Pandas DataFrame olarak alınması
- Sütun tiplerine göre otomatik grafik seçimi
- SQL sonuçlarının Gemini ile Türkçe yorumlanması
- Örnek analiz soruları
- Başarılı, boş ve hatalı sorguların PostgreSQL’e kaydedilmesi
- Hata yönetimi ve kullanıcı bilgilendirmeleri

## Dashboard Yapısı

Uygulama üç ana sekmeden oluşur.

### Genel Bakış

Genel Bakış sekmesi, e-ticaret işletmesinin temel performans göstergelerini sunar.

Bu bölümde aşağıdaki veriler bulunur:

- Toplam müşteri sayısı
- Toplam sipariş sayısı
- Toplam satış geliri
- Ortalama müşteri değerlendirme puanı
- Aylık satış grafiği
- En çok satılan 10 ürün kategorisi

Bu sekmenin amacı, işletmenin genel durumunun kısa sürede anlaşılmasını sağlamaktır.

### Detaylı Analiz

Detaylı Analiz sekmesi, sipariş ve müşteri davranışlarına ilişkin daha ayrıntılı görselleştirmeler içerir.

Bu bölümde:

- Ödeme yöntemi dağılımı
- Müşteri değerlendirme puanı dağılımı
- En fazla sipariş verilen eyaletler

gösterilir.

### AI Insights

AI Insights sekmesi, kullanıcının e-ticaret verileri hakkında doğal dilde soru sorabildiği yapay zekâ destekli analiz bölümüdür.

Kullanıcı sorusunu yazdıktan sonra sistem:

1. Veritabanı şemasını inceler.
2. Soruyu cevaplayacak PostgreSQL sorgusunu üretir.
3. SQL sorgusunu güvenlik kontrolünden geçirir.
4. Sorguyu PostgreSQL üzerinde çalıştırır.
5. Sonucu DataFrame olarak alır.
6. Uygun grafik türünü otomatik seçer.
7. Sonucu Gemini ile Türkçe olarak yorumlar.
8. Tüm analiz sürecini PostgreSQL’e kaydeder.

## Proje Akışı

```text
Kullanıcı doğal dilde soru sorar
                ↓
Veritabanı şeması SQLAlchemy ile çıkarılır
                ↓
Şema, kullanıcı sorusu ve SQL kuralları bir promptta birleştirilir
                ↓
Google Gemini PostgreSQL SELECT sorgusu üretir
                ↓
SQL sorgusu güvenlik kontrolünden geçirilir
                ↓
Güvenli sorgu PostgreSQL üzerinde çalıştırılır
                ↓
Sonuç Pandas DataFrame olarak alınır
                ↓
Sütun tiplerine göre uygun grafik otomatik seçilir
                ↓
Gemini sorgu sonucunu Türkçe olarak yorumlar
                ↓
Soru, SQL, sonuç ve analiz PostgreSQL’e kaydedilir
                ↓
Grafik, tablo ve AI analizi Streamlit arayüzünde gösterilir
