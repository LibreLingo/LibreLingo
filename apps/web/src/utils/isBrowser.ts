export default function isBrowser(): boolean {
  return new Boolean((process as unknown).browser).valueOf()
}
